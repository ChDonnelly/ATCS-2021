import pandas as pd
import pandas as pd
import string
import re
import numpy as np
from nltk.corpus import wordnet as wn
from itertools import product

from nltk.tag.stanford import StanfordNERTagger

import nltk
from collections import Counter



class resume_parser:

    def __init__(self,data):
        self.res = data['Resume_str'][0]



    def get_word_similarity_score(self,header_word,word):
        sem1,sem2 = wn.synsets(word),wn.synsets(header_word)
        maxscore = 0
        for i, j in list(product(*[sem1,sem2])):
            score = i.wup_similarity(j)
            maxscore = score if maxscore < score else maxscore
            return maxscore


#SOURCE: https://stackoverflow.com/questions/34460588/count-the-number-of-spaces-between-words-in-a-string
    def get_header_words(self):
        header_words_in_text =[]
        #self.res = self.res.replace(',','')

        self.res = self.res.replace('.','')
        self.res = self.res.replace(':','')
        self.res = self.res.replace(';','')
        self.res = self.res.replace(',','')
        all_words = self.res.split()
        sample_headers = ['education']
        for word in all_words:
            word_scores = []
            for header_word in sample_headers:
                score = self.get_word_similarity_score(header_word,word)
                if score == None:
                    score = 0
                word_scores.append(score)

            if (all(v == 0 for v in word_scores) == False):
                print("Header | " + sample_headers[word_scores.index(max(word_scores))] + "| ACTUAL | " + word)

        #https://stackoverflow.com/questions/3525953/check-if-all-values-of-iterable-are-zero
            #if (all(v == 0 for v in word_scores) == False): #If word_scores does not contain only zeros
               # print("Header | " + sample_headers.index(max(word_scores)) + "| ACTUAL | " + word)

'''
number_list = [1, 2, 3]
max_value = max(number_list) Return the max value of the list.
max_index = number_list. index(max_value) Find the index of the max value.
print(max_index)



'''



                #print(header_word," ",word,str(self.get_word_similarity_score(header_word,word)))

#https://www.codegrepper.com/code-examples/python/python+remove+commas+and+periods+from+string

'''
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



    def get_education(self):
        pass

    def get_age(self):
        pass




'''

















if __name__ == "__main__":



#https://stackoverflow.com/questions/58585052/find-most-common-substring-in-a-list-of-strings
    #data = pd.read_csv('Resume.csv')
    #parsy = resume_parser(data)
    #parsy.get_header_words()



    text = """Some economists have responded positively to Bitcoin, including
        Francois R. Velde, senior economist of the Federal Reserve in Chicago
        who described it as an elegant solution to the problem of creating a
        digital currency. In November 2013 Richard Branson announced that
        Virgin Galactic would accept Bitcoin as payment, saying that he had invested
        in Bitcoin and found it fascinating how a whole new global currency
        has been created, encouraging others to also invest in Bitcoin.
        Other economists commenting on Bitcoin have been critical.
        Economist Paul Krugman has suggested that the structure of the currency
        incentivizes hoarding and that its value derives from the expectation that
        others will accept it as payment. Economist Larry Summers has expressed
        a wait and see attitude when it comes to Bitcoin. Nick Colas, a market
        strategist for ConvergEx Group, has remarked on the effect of increasing
        use of Bitcoin and its restricted supply, noting, When incremental
        adoption meets relatively fixed supply, it should be no surprise that
        prices go up. And that’s exactly what is happening to BTC prices."""


    st = StanfordNERTagger('stanford-ner/english.all.3class.distsim.crf.ser.gz',
                           'stanford-ner/stanford-ner.jar')

    for sent in nltk.sent_tokenize(text):
        tokens = nltk.tokenize.word_tokenize(sent)
        tags = st.tag(tokens)
        for tag in tags:
            if tag[1] in ["PERSON", "LOCATION", "ORGANIZATION"]:
                print(tag)


