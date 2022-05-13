# Author: Chris Donnelly
# Due Date: 5/12/22

import pandas as pd
from nltk.corpus import wordnet as wn
from itertools import product
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import re


class resume_parser:

    def __init__(self, data):
        self.res = data['Resume_str'][0]

    # SOURCE: https://stackoverflow.com/questions/18871706/check-if-two-words-are-related-to-each-other/18872777#18872777
    # The function below finds the similarity of 2 words using the Wu-Palmer method (a method of counting 2 words' relatedness)

    def get_word_similarity_score(self, header_word, word):
        sem1, sem2 = wn.synsets(word), wn.synsets(header_word)
        maxscore = 0
        for i, j in list(product(*[sem1, sem2])):
            score = i.wup_similarity(j)
            maxscore = score if maxscore < score else maxscore
            return maxscore

    # SOURCE: https://stackoverflow.com/questions/34460588/count-the-number-of-spaces-between-words-in-a-string
    # The function below returns the indexes within the list of words in the résumé that are most similar to the sample résumé header words (like education, etc.)

    def get_top_indexes(self, sample_headers):
        # SOURCE: #https://www.codegrepper.com/code-examples/python/python+remove+commas+and+periods+from+string
        # The 4 lines below remove punctuation from the text so get_word_similarity_score() works properly
        self.res = self.res.replace('.', '')
        self.res = self.res.replace(':', '')
        self.res = self.res.replace(';', '')
        self.res = self.res.replace(',', '')
        all_words = self.res.split()  # Create list of words in résumé
        word_scores = []
        for word in all_words:  # Iterate through each word in list of words
            for header_word in sample_headers:
                score = self.get_word_similarity_score(header_word,word)  # Calculate similarity scores between each word in the text and the sample header words
                if score == None:
                    score = 0
                word_scores.append(score)
        top_score_indexes = []
        seen_indexes = []
        for i in range(10):  # Find the indexes of the top 10 words most similar to the sample headers
            index_of_max_score = word_scores.index(max(word_scores))
            if index_of_max_score not in seen_indexes:
                seen_indexes.append(index_of_max_score)
                top_score_indexes.append(index_of_max_score)
        top_score_indexes.sort()
        return [top_score_indexes, all_words]

    '''
    This function returns the sentences containing the words that are most similar to the 
    sample headers. This function's inputs require the execution of the previous function.
    '''

    def get_sentences(self, top_score_indexes, text_list):
        all_sentences = self.res.split('.')
        suggestion_sentences = []
        for index in top_score_indexes:
            # get word
            word = text_list[index]
            for sentence in all_sentences:
                if word in sentence:
                    suggestion_sentences.append(sentence)
        return suggestion_sentences

    # This function returns sentences containing numbers, or possible information on the experience on the résumé.
    def get_experience(self):
        suggestions = []  # List of sentences that will contain sentences with numbers
        sentences = self.res.split('.')
        for sentence in sentences:
            contains_number = [char.isdigit() for char in sentence]  # List of boolean values; true if a word has a number; false otherwise
            if True in contains_number:
                suggestions.append(sentence)

        return suggestions

    '''
    SOURCE: https://unbiased-coder.com/extract-names-python-nltk/
    This functions uses nltk to return the names of people in a given sentence.
    This name extraction code is helpful because nltk often extracts the names of states and people which 
    colleges are named after.
    '''

    def check_name(self, sentence):
        names_in_resume = []
        name_types = []
        nltk_results = ne_chunk(pos_tag(word_tokenize(sentence)))
        for nltk_result in nltk_results:
            if type(nltk_result) == Tree:
                name = ''
                for nltk_result_leaf in nltk_result.leaves():
                    name += nltk_result_leaf[0] + ' '
                names_in_resume.append(name)


        return names_in_resume  # Return a list of names in the résumé

    '''
    SOURCES: https://stackoverflow.com/questions/19350900/finding-all-unique-words-from-a-list-using-loops, https://stackoverflow.com/questions/6531482/how-to-check-if-a-string-contains-an-element-from-a-list-in-python
    This function uses the sentences found in the get_sentences() function and returns the words from these sentences that contain 
    educational substrings like "ollege" (from "college") and "niversity" (from "university"), etc. These substrings are used to catch specific cases involving upper or lower case letters.
    '''

    def get_education(self, sentences):
        suggestions = []
        colleges_in_text = []
        for sentence in sentences:
            colleges_in_text.extend(self.check_name(sentence))
        education_words = ["ollege", "niversity", "tate"]
        for college in colleges_in_text:
            if len([i for i in education_words if i in college]) > 0:
                suggestions.append(college)

        unique_suggestions = []  # The folowing code removes duplicate strings from the eduaction-related suggestions of words.
        for i in suggestions:
            if not i in unique_suggestions:
                unique_suggestions.append(i)
        return unique_suggestions

    '''
    SOURCE: https://www.geeksforgeeks.org/python-remove-unwanted-spaces-from-string/
    The following function is the driver function of the resume_parser class that runs
    all other functions and formats their outputs.
    '''

    def get_info(self):
        indexes_return = self.get_top_indexes(['Education'])
        education_sentences = self.get_sentences(indexes_return[0], indexes_return[1])
        education_suggestions = self.get_education(education_sentences)
        experience_suggestions = self.get_experience()
        educ_str = ""
        exp_str = ""
        for i in education_suggestions:
            educ_str += i
            educ_str += " | "
        for i in experience_suggestions:
            exp_str += i
            exp_str += " | "
        educ_str = re.sub(' +', ' ', educ_str)
        exp_str = re.sub(' +', ' ', exp_str)
        print("APPLICANT INFORMATION:")
        print("_________________________________")
        print("EDUCATION:")
        print("Results from résumé:")
        print(educ_str)
        print("_________________________________")
        print("EXPERIENCE:")
        print("Results from résumé:")
        print(exp_str)
        print("_________________________________")


if __name__ == "__main__":
    data = pd.read_csv('Resume.csv')
    parsy = resume_parser(data)
    print(parsy.get_info())








