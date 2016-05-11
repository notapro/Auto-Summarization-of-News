'''
Created on Feb 21, 2016

@author: Sameer, pro
'''
import sys
sys.path.append('/home/pro/PycharmProjects/text_summ/Auto-Summarization-of-News')
from Code.Tokenizer import Tokenizer
from Code.Chain_Scoring import Chain_Scoring
from Code.Extractor import Extractor
from Code.Sentence_Scorer import Sentence_Scorer
from Code.Pronoun_Resolver import Pronoun_Resolver


def main():
    
    current_sentence_num = 0
    lexical_chain = {}    
    word_sentence = {}  
    word_count = {} 
    input_file = "../Input Files/input_file1.txt"
    output_file = "../Output Files/OutputFile1.txt"

    lexical_chain = {}
    word_sentence = {}
    noun_count = {}
    resolve_pronouns = True
    tokenizer_object = Tokenizer()
    scoring_object = Chain_Scoring()
    extractor_object = Extractor()
    pronoun_resolver = Pronoun_Resolver()

    try:
        text = tokenizer_object.get_text(input_file)
        sentences_original = tokenizer_object.extract_sentences(text)

        if resolve_pronouns is True:
            sentences = pronoun_resolver.resolve(text)
        else:
            sentences = sentences_original

        proper_nouns_count = {}
        proper_noun_sentences = {}

        for sentence in sentences:

            current_sentence_num += 1
            tagged_words = tokenizer_object.extract_tagged_words_from_sentence(sentence)
            
            extractor_object.add_proper_nouns(tagged_words, proper_nouns_count, proper_noun_sentences , current_sentence_num )
            
            word_count = tokenizer_object.generate_noun_frequency(tagged_words, word_sentence, word_count)
            lexical_chain = tokenizer_object.generate_lexical_chain(tagged_words, word_sentence, lexical_chain)
            word_sentence = tokenizer_object.generate_word_to_sentence_map(tagged_words, word_sentence, current_sentence_num)
       
            
        
        lexical_chain_scores = scoring_object.score_lexical_chain(lexical_chain, word_count)
        strong_synsets = scoring_object.get_strong_synsets(lexical_chain_scores)        
        strong_sentence_numbers = extractor_object.get_strong_sentence_numbers(strong_synsets, lexical_chain, word_sentence, word_count)
        extractor_object.extract_strong_sentences(sentences, strong_sentence_numbers, output_file)
        sentence_scorer = Sentence_Scorer()
        strong_sentence_nums = sentence_scorer.score(strong_synsets, lexical_chain,sentences,word_sentence)
        
        print("normal strong sentences {}".format(strong_sentence_nums))
        
        strong_proper_nouns_sentences = extractor_object.get_strong_proper_noun_sentences(proper_noun_sentences, proper_nouns_count, current_sentence_num)
        
        print("proper noun sentences {}".format(strong_proper_nouns_sentences))
        
        strong_sentence_nums = list(set(strong_sentence_nums).union(strong_proper_nouns_sentences))
        
        strong_sentence_nums.append(0)
        
        unique_sentences = [ii for n, ii in enumerate(strong_sentence_nums) if ii not in strong_sentence_nums[:n]]
        
        print(unique_sentences)
        
        target = open(output_file,'w')
        
        target.truncate()
        
        for sentence_num in sorted(unique_sentences):
            print(sentences[sentence_num]+"\n")
            target.write(sentences[sentence_num] + "\n")
            
        target.close()
        
    except FileNotFoundError as e:

        print(str(e))


if __name__ == "__main__":
    main()
