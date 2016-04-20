'''
Created on Feb 21, 2016

@author: Sameer, pro
'''

from Tokenizer import Tokenizer
from Chain_Scoring import Chain_Scoring
from Extractor import Extractor
from tp import Sentence_Scorer

def main():
    
    current_sentence_num = 0
    lexical_chain = {}    
    word_sentence = {}  
    word_count = {} 
    input_file = "Input Files/InputFile1.txt"
    output_file = "Output Files/OutputFile1.txt"

    lexical_chain = {}
    word_sentence = {}
    noun_count = {}
    
    tokenizer_object = Tokenizer()
    scoring_object = Chain_Scoring()
    extractor_object = Extractor()

    
    
    try:

        sentences = tokenizer_object.extract_sentences(input_file)

        for sentence in sentences:

            current_sentence_num += 1
            tagged_words = tokenizer_object.extract_tagged_words_from_sentence(sentence)
            word_count = tokenizer_object.generate_noun_frequency(tagged_words, word_sentence, word_count)
            lexical_chain = tokenizer_object.generate_lexical_chain(tagged_words, word_sentence, lexical_chain)
            word_sentence = tokenizer_object.generate_word_to_sentence_map(tagged_words, word_sentence, current_sentence_num)
            

        # print("\nPrinting Lexical Chain\n")

        # for key, value in lexical_chain.items():

        #     print(key, value)

        # print("\nPrinting word sentence mapping\n")

        # for key, value in word_sentence.items():

        #     print(key, value)

        # print("\nNoun Count\n")

        # for key, value in word_count.items():

        #     print(key, value)
            
        
        lexical_chain_scores = scoring_object.score_lexical_chain(lexical_chain, word_count)        
        strong_synsets = scoring_object.get_strong_synsets(lexical_chain_scores)        
        strong_sentence_numbers = extractor_object.get_strong_sentence_numbers(strong_synsets, lexical_chain, word_sentence, word_count)
        extractor_object.extract_strong_sentences(sentences, strong_sentence_numbers, output_file)
        sentence_scorer = Sentence_Scorer()
        sentence_scorer.score(strong_synsets,lexical_chain,sentences,word_sentence)

    except FileNotFoundError as e:

        print(str(e))


if __name__ == "__main__":
    main()
