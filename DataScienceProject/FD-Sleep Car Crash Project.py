#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
Data Science Final Project: How Does Sleep Affect the Likelihood of Getting in a Car Crash?
Name: Chris Donnelly
Date: 12/7/21

"""


# In[3]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


# In[4]:


df = pd.read_csv('sleep_car_crashes_data_set.csv')


# In[5]:


"""
Overview: This code converts the columns with numerical data into floats (just in case they were registered as objects or strings in the .csv file)
"""

for column in df.columns:
    if (column != 'state' and column != 'observes_daylight_savings' and column != 'greater_than_median_density'):
        df[column] = df[column].astype(float)
"""
df['adults_reporting_insufficient_sleep'] = df['adults_reporting_insufficient_sleep'].astype(float)
df['fatal_crashes'] = df['fatal_crashes'].astype(float)
df['total_vehicle_miles'] = df['total_vehicle_miles'].astype(float)
df['caffeination_ranking'] = df['caffeination_ranking'].astype(float)
df['stress'] = df['stress'].astype(float)
df['average_commute_time'] = df['average_commute_time'].astype(float)
df['alcohol_consumption'] = df['alcohol_consumption'].astype(float)

"""



# In[6]:


"""
Visualization #1: Scatterplot


"""

sns.scatterplot(data=df,x="adults_reporting_insufficient_sleep",y="fatal_crashes").set(title='Fatal Car Crashes vs. Percentage of Adults Reporting Insufficient Sleep (%)',xlabel='Percentage of Adults Reporting Insufficient Sleep (%)',ylabel='Fatal Car Crashes')
print("Correlation: " + str(df['fatal_crashes'].corr(df['adults_reporting_insufficient_sleep'])))


# In[7]:


"""
Overview: This is a function that determines and returns the best central tendency
statistic based on a dataframe column's number of outliers. This method considers outliers values
that are less than or more than 1.5 times less and 1.5 times more than the interquartile range of the dataframe
column.

Purpose: Even small outliers can drastically change the mean of a dataset, and certain central tendency metrics are 
better than others. This function makes it easier to determine and find which one is best for a dataframe column.

Parameters
---
column_name: str
    The name of a dataframe column (the column must have numerical data)
    
Returns
---
np.median(df[column_name]) or np.median(df[column_name]): float
    The function returns the median of the column if the column has more than 6 outliers, and its mean otherwise.

"""

def central_tendency_stat(column_name):

    outlier_counter = 0
    quart_1 = np.percentile(df[column_name],25)
    quart_3 = np.percentile(df[column_name],75)
    IQR = quart_3 = quart_1
    for _,value in df[column_name].iteritems(): #QUESTION: Is there a more efficient way to iterate through
        if value < (quart_1 - (IQR * 1.5)) or value > (quart_3 + (IQR * 1.5)):
            outlier_counter +=1
    if outlier_counter > 6:
        return np.median(df[column_name])
    else:
        return np.mean(df[column_name])


# In[8]:


"""
Overview: This function uses the previous method to determine outliers of whether a value is less than or greater than 1.5 times the interquartile range.
The function then removes the outliers from the dataframe series. If two series variables are passed as parameters,
the function will remove outliers from the first series and the values at the corresponding indexes in series2 (so that when 
they are graphed, they are the same length)

Parameters
---
series: str
    The name of the pandas series from which outliers should be removed
    
series2: str
    The names of the pandas series with corresponding indexes that should 
    be removd
    
Returns
---
Nothing: This function modifies series and series2——it does not return anything.


"""

def removeOutliers(series,series2=None):
    quart_1 = np.percentile(series,25)
    quart_3 = np.percentile(series,75)
    IQR = quart_3 = quart_1
    for i in range(len(series)):
         if series[i] < (quart_1 - (IQR * 1.5)) or series[i] > (quart_3 + (IQR * 1.5)): 
                series.drop(i)
                if (type(series2) != None):
                    series2.drop(i)


# In[9]:


"""
Overview: This code cell iterates through each state and certain variables per column. It then checks whether a state's value
in a column is greater than the column's central tendency metric. If so, a counter is incremented. At the end of the inner loop,
the counter is added to a list (outlier_column_counter). This has 50 int elements; each corresponding to the number of columns
in which a certain state is an outlier. For example, if outlier_column_counter[0] = 3, then Alabama would have 3 pieces of data that 
are greater than their columns' central tendency.


Purpose: Several factors besides sleep influence a state's number of fatal car crashes. This function indicates how many
variables per state are greater than the mean or median. This function allows us to disregard the states that have several variables
(like a high population density) that could influence fatal_crashes.

"""
column_indexes_not_used = [2,5]
outlier_column_counter = None
entered=None
outlier_values_per_state = []
for column_index in range(len(df)):
    entered = False
    for row_index in range(1,len(df.columns)):
        outlier_column_counter = 0
        curr_val = df.iloc[column_index,row_index]
        if(row_index in column_indexes_not_used):
            continue
        else:
            curr_val_type = df.columns[row_index]
            if (curr_val > central_tendency_stat(curr_val_type)):
                entered = True
                outlier_column_counter += 1
    outlier_values_per_state.append(outlier_column_counter)
  


# In[10]:



"""
Overview: This code iterates through the the list of outlier values per state and appends the names of the states
that have 0 outlier values to a new list called states_without_outlier_values.


"""
states_without_outlier_values = []
for i in range(len(outlier_values_per_state)):
    if (outlier_values_per_state[i] < 1):
        states_without_outlier_values.append(df["state"][i])
        
        


# In[11]:


#create data science folder inside ATCS-2021 and then put .py file into that and fo
"""
Overview: This code creates new lists of sleep data and car crash data for 
states that do not have variables greater than their corresponding columns' mean or median.

"""
new_sleep_data = []
new_car_crash_data = []
for state_index in range(len(df['state'])):
    if(df['state'][state_index] in states_without_outlier_values):
        new_sleep_data.append(df['adults_reporting_insufficient_sleep'][state_index])
        new_car_crash_data.append(df['fatal_crashes'][state_index])


# In[12]:


"""
Overview: This code cell creates a new dataframe with the sleep and car crash data from states that do not have
several outleir variables.
"""
df2 = pd.DataFrame({'adults_reporting_insufficient_sleep': new_sleep_data,'fatal_crashes': new_car_crash_data})


# In[13]:


"""
Visualization #2: Scatterplot
"""

sns.scatterplot(data=df,x="total_vehicle_miles",y='fatal_crashes').set(title = 'Fatal Car Crashes vs. Total Vehicle Miles (mi)',xlabel ='Total Vehicle Miles (mi)',ylabel='Fatal Car Crashes')
print("Correlation: " + str(df['fatal_crashes'].corr(df['total_vehicle_miles'])))


# In[14]:


"""
Visualization #3: Pie Chart

Overview: This code cell creates a pie chart showing the percentages of car crashes in 
states that have a greater or lesser population density that the median population density for all 50 states.

Purpose: This visualization shows that, since states with a higher population density are responsible for more fatal car crashes,
other variables influence the fatal_crashes.
"""


x_labels = ['Greater than','Less than']
y_labels = [df.loc[df['greater_than_median_density']==True,'fatal_crashes'].sum(), df.loc[df['greater_than_median_density']==False,'fatal_crashes'].sum()]
plt.pie(y_labels,labels=x_labels,colors=['royalblue','tomato'],autopct="%1.0f%%")
plt.title("Fatal Car Crashes vs. Greater than Median Population Density")
plt.show()


# In[15]:


"""
Visualization #4: Scatterplot
"""
sns.scatterplot(data=df2,x="adults_reporting_insufficient_sleep",y="fatal_crashes").set(title='Fatal Car Crashes vs. Percentage of Adults Reporting Insufficient Sleep (%)',xlabel='Percentage of Adults Reporting Insufficient Sleep (%)',ylabel='Fatal Car Crashes')
print("Correlation: " + str(df2['fatal_crashes'].corr(df2['adults_reporting_insufficient_sleep'])))


# In[ ]:




