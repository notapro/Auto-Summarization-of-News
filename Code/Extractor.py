'''
Created on Apr 6, 2016

@author: Sameer
'''

class Extractor:    
    
    
    def get_strong_sentence_numbers(self, strong_synsets, lexical_chain, word_sentence, word_count):
        
        sentence_numbers = set ()
        
        for synset in strong_synsets:
            
            if(lexical_chain.__contains__(synset)):
                
                words_in_chain = lexical_chain[synset]
                
                length = 0.0
                
                for word in words_in_chain:
                    
                    length += word_count[word.lower()]
                
                avg_length = length/len(words_in_chain)
                                
                for word in words_in_chain :
                    
                    if(word_count[word] >= avg_length):
                        
                        first_sentence_num = word_sentence[word.lower()][0]
                
                        sentence_numbers.add(first_sentence_num)
                        
                        break                    
                                
            else:
                
                raise KeyError ("Strong Synset not found in lexical chain")
            
        #print (sentence_numbers)
        
        return sentence_numbers
    
    def extract_strong_sentences(self, sentences, strong_sentence_numbers, output_file):
        
        target = open(output_file,'w')
        
        target.truncate()
        
        for sentence_num in sorted(strong_sentence_numbers):
            
            target.write (sentences[sentence_num-1] + " ")
            #print (sentences[sentence_num-1] + " ")
            
        target.close()