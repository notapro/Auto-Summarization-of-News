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
        
        
    def add_proper_nouns(self, tagged_words, proper_nouns_count, proper_noun_sentences, current_sentence_num):
        
        for word_tag in tagged_words:
            
            if(word_tag[1]=="NNP"):
                
                print("got a proper noun {}".format(word_tag[0]))
                
                if(proper_nouns_count.__contains__(word_tag[0].lower())):
                    
                    count = proper_nouns_count.get(word_tag[0].lower())
                    count = count + 1
                    proper_nouns_count[word_tag[0].lower()] = count
                    
                    sentence_nums = proper_noun_sentences.get(word_tag[0].lower())
                    sentence_nums.append(current_sentence_num-1)
                    proper_noun_sentences[word_tag[0].lower()] = sentence_nums
        
                else:
                    
                    proper_nouns_count[word_tag[0].lower()] = 1
                    sentence_nums = [current_sentence_num-1]
                    proper_noun_sentences[word_tag[0].lower()] = sentence_nums
        
        
    def get_strong_proper_noun_sentences(self, proper_noun_sentences, proper_nouns_count, num_sentences):
        
        total_count = 0
        total_proper_nouns = 0
        
        strong_proper_nouns_sentences = []
        
        
        for key, value in proper_nouns_count.items():
            
            if (value >= num_sentences/3):
                strong_proper_nouns_sentences.append(proper_noun_sentences[key][0])
                  
        
        return strong_proper_nouns_sentences
        
        
        
        
        
        
        
        
        
        
        
        
        