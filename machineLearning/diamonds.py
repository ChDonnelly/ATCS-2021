
''' Import Statements '''
# General Imports
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Linear Regression Imports
from sklearn.linear_model import LinearRegression

# Logistic Regression Imports
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

"""
diamonds: predict cut (logr) or could do mar
alcohol: predict cirrhosis death rate (multi regression)
employees: predict if someone will leave the country (logistic regression)
homicides: mlr predict murders per year per million
houses: mlr predict selling prices
"""


''' Load the Data '''

diamonds = pd.read_csv("Data/diamonds.csv")
drinking = pd.read_csv("Data/drinking.csv")
employees = pd.read_csv("Data/employees.csv")
homicides = pd.read_csv("Data/homicides.csv")
houses = pd.read_csv("Data/houses.csv")

# Get Data and Split Into Training Data