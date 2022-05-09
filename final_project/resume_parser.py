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
    def get_related_section(self):
        header_words_in_text =[]
        #self.res = self.res.replace(',','')

        self.res = self.res.replace('.','')
        self.res = self.res.replace(':','')
        self.res = self.res.replace(';','')
        self.res = self.res.replace(',','')
        all_words = self.res.split()
        sample_headers = ['education']
        word_scores = []
        for word in all_words:
            for header_word in sample_headers:
                score = self.get_word_similarity_score(header_word,word)
                if score == None:
                    score = 0
                word_scores.append(score)

        top_score_indexes = []
        seen = []
        for i in range(10):
            index_of_max_score = word_scores.index(max(word_scores))
            if index_of_max_score not in seen:
                seen.append(index_of_max_score)
                top_score_indexes.append(index_of_max_score)

        top_score_indexes.sort()
        return [top_score_indexes, all_words]
        #return [word_scores[i] for i in top_ten_score_indexes]





        #after get header words related to education, find sections between those
        #other method will look for name sof colleges that will match



    def get_sections(self,top_score_indexes, text_list):
        if len(top_score_indexes) == 1:
            print([text_list[i] for i in range(top_score_indexes[0]-20,top_score_indexes[0]+20)])
        else:
            words_in_between_list =[]
            for i in range(len(top_score_indexes)-1):
                first_index = top_score_indexes[i]
                last_index = top_score_indexes[i + 1] + 1
                section = text_list[slice(first_index,last_index)]
                words_in_between_list.extend(section)
            words_in_between_list.extend(text_list(slice(top_score_indexes[len(top_score_indexes) - 1]),len(text_list)))
            print(words_in_between_list)







        '''
        sections = {}

        for i in range(len(header_word_list)-1):
            begin_word = header_word_list[i]
            end_word = header_word_list[i+1]
            stringx = str(begin_word) + "(.*)" + str(end_word)
            result = re.search(stringx, self.res)

            if result != None:
                sections[begin_word] = result.group()

        return sections
'''
    def do_it(self):
        x = self.get_related_section()
        self.get_sections(x[0], x[1])




            
        


        #https://stackoverflow.com/questions/3525953/check-if-all-values-of-iterable-are-zero
            #if (all(v == 0 for v in word_scores) == False): #If word_scores does not contain only zeros
               # print("Header | " + sample_headers.index(max(word_scores)) + "| ACTUAL | " + word)







                #print(header_word," ",word,str(self.get_word_similarity_score(header_word,word)))

#https://www.codegrepper.com/code-examples/python/python+remove+commas+and+periods+from+string
















if __name__ == "__main__":




#https://stackoverflow.com/questions/58585052/find-most-common-substring-in-a-list-of-strings
    data = pd.read_csv('Resume.csv')
    parsy = resume_parser(data)
    parsy.do_it()










