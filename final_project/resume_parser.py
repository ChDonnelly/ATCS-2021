import pandas as pd
import pandas as pd
import string
import re

from nltk.corpus import wordnet as wn
from itertools import product


def self(args):
    pass


class resume_parser:

    def __init__(self,resume_data):
        self.data = resume_data
        #self.curr_resume_index = 0
        self.res = self.data['Resume_str'][0]

#SOURCE: https://stackoverflow.com/questions/34460588/count-the-number-of-spaces-between-words-in-a-string
    def get_resume_metrics(self):
        counter = 0
        header_words_in_text = []
        all_words = self.res.split()

        sample_headers = ['Summary', 'Experience,', 'Highlights', 'Accomplishments', 'Achievement']
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

            if (len([i for i in word_scores if i >= 0.8]) >= 1):
                header_words_in_text.append(word)
        return header_words_in_text



    def get_words_between(self,header_word_list):
        sections = {}

        for i in range(len(header_word_list)-1):
            begin_word = header_word_list[i]
            end_word = header_word_list[i+1]
            stringx = str(begin_word) + "(.*)" + str(end_word)
            result = re.search(stringx, self.res)
            print(result['match'])

        '''
        import re

        s = 'asdf=5;iwantthis123jasd'
        result = re.search('asdf=5;(.*)123jasd', s)
        print(result.group(1))
        '''




    def to_string(self):
        print(self.data['Resume_str'][0].p())



if __name__ == "__main__":






    data = pd.read_csv('Resume.csv')

    parser = resume_parser(data)

    header_words_in_text = parser.get_resume_metrics()
    print(parser.get_words_between(header_words_in_text))
    #print(parser.get_resume_metrics())



    #s = 'asdf=5;iwantthis123jasdasl;dhg'
    #result = re.search('asdf=5;(.*)123jasd', s)
    #print(result.group(1))





