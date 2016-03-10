'''
Created on Feb 21, 2016

@author: Sameer
'''
import nltk
from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.corpus import wordnet as wn



class Tokenizer:
    
    '''
    This class handles extracting words from documents and parts of speech tagging.
    '''

    
    def __init__(self):
        self.words = []
        pass
        
        
    def extract_words(self,file_name):
        
        try:
            file_content = open(file_name, 'r').read()
            
            #print (file_content) 
            
            #example = "This is sentence 1. This is sentence 2."         
            
            sentences = sent_tokenize(file_content, 'English')             
            
            #print (sentences)
            
            current_sentence_num = 0
            
            lexical_chain = {}
            
            word_sentence = {}
            
            chain_categories = ("NN" , "NNS")
            
            for sentence in sentences :
                
                #print(sentence)
                
                current_sentence_num += 1
                tagged_words = nltk.pos_tag(word_tokenize(sentence, 'English'))  # @UndefinedVariable
                
                print (tagged_words)
                
                for word_tag in tagged_words:                    
                    
                    
                    if(word_tag[1] in chain_categories):                        
                                      
                        #print (word_tag)
                        
                        if(word_sentence.__contains__(word_tag[0].lower())):
                                
                                sentence_numbers = word_sentence.get(word_tag[0].lower())
                                sentence_numbers.append(current_sentence_num)
                                word_sentence[word_tag[0].lower()] = sentence_numbers
                            
                        else :
                                
                            sentence_numbers = [current_sentence_num]
                            word_sentence[word_tag[0].lower()] = sentence_numbers
                        
                        
                            for synset in wn.synsets(word_tag[0], pos = wn.NOUN):  # @UndefinedVariable
                         
                                #print (synset)
                                
                                if(lexical_chain.__contains__(synset)):
                                    
                                    noun_list = lexical_chain.get(synset)
                                    noun_list.append(word_tag[0])
                                    lexical_chain[synset] = noun_list
                                
                                else :
                                    
                                    noun_list = [word_tag[0]]
                                    lexical_chain[synset] = noun_list
            
            print ("\nPrinting Lexical Chain\n")               
                            
            for key, value in lexical_chain.items():
                    
                print (key, value)
            
            print("\nPrinting word sentence mapping\n")                   
            
            for key, value in word_sentence.items():
                
                print (key, value)   
              
        
        except FileNotFoundError as e:
            
            print(str(e))