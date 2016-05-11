'''
Created on Feb 21, 2016

@author: Sameer, pro
'''
import nltk
from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.corpus import wordnet as wn


class Tokenizer:
    
    '''
    This class handles extracting words from documents and parts of speech tagging.
    '''
    chain_categories = ("NN" , "NNS")

    def __init__(self):
        self.words = []
        pass
        
    def extract_sentences(self, file_content):

        # print(file_content)
        sentences = sent_tokenize(file_content, 'English')
        # print(sentences)
        return sentences

    def get_text(self, file_name):
        file_content = open(file_name, 'r').read()
        return file_content


    def extract_tagged_words_from_sentence(self, sentence):

        tagged_words = nltk.pos_tag(word_tokenize(sentence, 'English'))  # @UndefinedVariable
        # print(tagged_words)
        return tagged_words

    def generate_word_to_sentence_map(self, tagged_words, word_sentence, current_sentence_num):

        for word_tag in tagged_words:

            if word_tag[1] in self.chain_categories:

                # print(word_tag)

                if word_sentence.__contains__(word_tag[0].lower()):

                    sentence_numbers = word_sentence.get(word_tag[0].lower())
                    sentence_numbers.append(current_sentence_num)
                    word_sentence[word_tag[0].lower()] = sentence_numbers

                else:

                    sentence_numbers = [current_sentence_num]
                    word_sentence[word_tag[0].lower()] = sentence_numbers

        return word_sentence

    def generate_noun_frequency(self, tagged_words, word_sentence, word_count):
        

        for word_tag in tagged_words:

            if word_tag[1] in self.chain_categories:

                # print(word_tag)

                if word_sentence.__contains__(word_tag[0].lower()):

                    word_count[word_tag[0].lower()] += 1

                else:

                    word_count[word_tag[0].lower()] = 1

        return word_count

    def generate_lexical_chain(self, tagged_words, word_sentence, lexical_chain):

        for word_tag in tagged_words:

            if word_tag[1] in self.chain_categories:

                # print(word_tag)

                if word_tag[0].lower() not in word_sentence:

                    for synset in wn.synsets(word_tag[0], pos=wn.NOUN):  # @UndefinedVariable

                        # print(synset)

                        if lexical_chain.__contains__(synset):

                            noun_list = lexical_chain.get(synset)
                            noun_list.append(word_tag[0].lower())
                            lexical_chain[synset] = noun_list

                        else:

                            noun_list = [word_tag[0].lower()]
                            lexical_chain[synset] = noun_list

        return lexical_chain