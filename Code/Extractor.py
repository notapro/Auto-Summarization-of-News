'''
Created on Apr 6, 2016

@author: Sameer
'''
class Extractor:
    
    def get_strong_sentence_numbers(self, strong_synsets, lexical_chain, word_sentence):
        
        sentence_numbers = set ()
        
        for synset in strong_synsets:
            
            if(lexical_chain.__contains__(synset)):
                
                first_word = lexical_chain[synset][0]
                
                first_sentence_num = word_sentence[first_word][0]
                
                sentence_numbers.add(first_sentence_num)
                
            else:
                
                raise KeyError ("Strong Synset not found in lexical chain")
            
        
        return sentence_numbers
    
    def extract_strong_sentences(self, sentences, strong_sentence_numbers, output_file):
        
        target = open(output_file,'w')
        
        target.truncate()
        
        for sentence_num in sorted(strong_sentence_numbers):
            
            target.write (sentences[sentence_num-1])
            print (sentences[sentence_num-1])
            
        target.close()