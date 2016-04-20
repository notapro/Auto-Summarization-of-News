'''
Created on Apr 6, 2016

@author: Sameer
'''

import statistics

class Chain_Scoring:

    def score_lexical_chain(self,lexical_chain, noun_count):
        
        chain_score = {}
        #print("\nChain Scores\n")

        for synset, words in lexical_chain.items():

            length = 0.0
            
            for word in words:

                length += noun_count[word]

            
            homogeneity = 1-(len(words)/length)

            chain_score[synset] = length*homogeneity

            #print(synset, chain_score[synset])
        
        return chain_score
    
    def get_strong_synsets(self, lexical_chain_scores):
        
        strong_synsets = []
        
        chain_scores = []
        
        for synset, score in lexical_chain_scores.items():
            
            chain_scores.append(score)
            
        
        chain_stand_dev = statistics.pstdev(chain_scores, mu=None)
        
        chains_mean_score = statistics.mean(chain_scores)
        
        for synset, score in lexical_chain_scores.items():
            
            if (score > (chains_mean_score + 2 * chain_stand_dev)):
                
                strong_synsets.append(synset)
                
        print ("\n\n\Printing Strong Chains \n\n")
                
        #print (strong_synsets)
                
        return strong_synsets
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
        