import pandas as pd
import pandas as pd
import string
import re
from itertools import product

from nltk.corpus import wordnet

class resume_parser:

    def __init__(self,resume_data):
        self.data = resume_data
        #self.curr_resume_index = 0

#SOURCE: https://stackoverflow.com/questions/34460588/count-the-number-of-spaces-between-words-in-a-string
    def get_resume_metrics(self):
        res = self.data['Resume_str'][0]
        res.strip(' ')
        #----
        spaces = re.findall('\s+',res)
        words = res.split()
        print("spaces:",spaces)
        print("words:",words)

        for i in range(len(spaces)):
            if len(spaces[i]) > 5:
                if i != 0:
                    print("word before: " + str(words[i-1]))
                #if i < len(words)-1:
                #    print("word after: " + str(words[i+1]))
                print("_____________________")
                print(" ")




        #space between word 0 and 1 is at index 0

        #for i in range(0,len(tokens)):
        #    print(len(tokens[i]))








if __name__ == "__main__":
    #data = pd.read_csv('Resume.csv')

    #parser = resume_parser(data)

    #parser.get_resume_metrics()



    list1 = ['Compare', 'require']
    list2 = ['choose', 'copy', 'define', 'duplicate', 'find', 'how', 'identify', 'label', 'list', 'listen', 'locate',
             'match', 'memorise', 'name', 'observe', 'omit', 'quote', 'read', 'recall', 'recite', 'recognise', 'record',
             'relate', 'remember', 'repeat', 'reproduce', 'retell', 'select', 'show', 'spell', 'state', 'tell', 'trace',
             'write']
    list = []

    for word1 in list1:
        for word2 in list2:
            wordFromList1 = wordnet.synsets(word1)
            wordFromList2 = wordnet.synsets(word2)
            if wordFromList1 and wordFromList2:  # Thanks to @alexis' note
                s = wordFromList1[0].wup_similarity(wordFromList2[0])
                list.append(s)

    print(max(list))





