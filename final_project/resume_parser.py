import pandas as pd
import pandas as pd
import string
import re
import numpy as np
from nltk.corpus import wordnet as wn
from itertools import product


from collections import Counter



class resume_parser:

    def __init__(self,resume_data):
        self.data = resume_data
        self.res = self.data['Resume_str'][0]
        self.header_words = np.unique(self.get_header_words())
        self.sections = self.get_sections(self.header_words)




#SOURCE: https://stackoverflow.com/questions/34460588/count-the-number-of-spaces-between-words-in-a-string
    def get_header_words(self):
        header_words_in_text =[]
        all_words = self.res.split()

        sample_headers = ['Summary', 'Experience,', 'Highlights', 'Accomplishments', 'Achievements','skills','education','University','Company']
        for word in all_words:
            word_scores = []
            for header_word in sample_headers:
                #get score
                sem1, sem2 = wn.synsets(word), wn.synsets(header_word)
                maxscore = 0
                for i, j in list(product(*[sem1, sem2])):
                    score = i.wup_similarity(j)  # Wu-Palmer Similarity
                    maxscore = score if maxscore < score else maxscore
                    word_scores.append(maxscore)

            #https: // stackoverflow.com / questions / 30944577 / check - if -string - is - in -a - pandas - dataframe
            if (len([i for i in word_scores if i >= 0.8]) >= 1):
                #check if word in other csv's:
                #word_count = self.data['Resume_str'].str.contains(word).sum()
                #if word_count >=  800: #TINKER WITH LEN(SELF.DATA) TO CHANGE FREQUENCY OF WORD OCURRENCE
                header_words_in_text.append(word)
        return header_words_in_text


    def get_sections(self,header_word_list):

        sections = {}

        for i in range(len(header_word_list)-1):
            begin_word = header_word_list[i]
            end_word = header_word_list[i+1]
            stringx = str(begin_word) + "(.*)" + str(end_word)
            result = re.search(stringx, self.res)

            if result != None:
                sections[begin_word] = result.group()

            

        return sections

    def process_all_resumes(self):
        str_long = ""

        for i in range(len(self.data)):
            mini_str = self.data['Resume_str'][i]
            str_long += mini_str


        l = str_long.split()

        c = Counter(l)
        for i in range(50):
            print(str(c.most_common(i)))






#https://www.tutorialspoint.com/list-frequency-of-elements-in-python











        #create an empty dataframe
        #iterate through resumes
        #get the highlighted keywords that ARE PRESENT IN THE RESUME
        #Make those the columns of dataframe
        #put the sections in to the corresponding columns





















if __name__ == "__main__":


#https://stackoverflow.com/questions/58585052/find-most-common-substring-in-a-list-of-strings
    data = pd.read_csv('Resume.csv')
    parsy = resume_parser(data)
    print(parsy.sections)


    #parsy = resume_parser(data)
    #print(len(parsy.header_words_in_text))
    #print(len(parsy.header_words_in_text))
    #print(parsy.process_all_resumes())

