'''
Created on Feb 21, 2016

@author: Sameer, pro
'''
from Code.Tokenizer import Tokenizer


def main():
    
    current_sentence_num = 0
    lexical_chain = {}
    word_sentence = {}
    noun_count = {}
    input_file = "../Input Files/InputFile1.txt"
    tokenizer_object = Tokenizer()
    
    try:

        sentences = tokenizer_object.extract_sentences(input_file)

        for sentence in sentences:

            current_sentence_num += 1
            tagged_words = tokenizer_object.extract_tagged_words_from_sentence(sentence)
            noun_count = tokenizer_object.generate_noun_frequency(tagged_words, word_sentence, noun_count)
            lexical_chain = tokenizer_object.generate_lexical_chain(tagged_words, word_sentence, lexical_chain)
            word_sentence = tokenizer_object.generate_word_to_sentence_map(tagged_words, word_sentence, current_sentence_num)

        print("\nPrinting Lexical Chain\n")

        for key, value in lexical_chain.items():

            print(key, value)

        print("\nPrinting word sentence mapping\n")

        for key, value in word_sentence.items():

            print(key, value)

        print("\nNoun Count\n")

        for key, value in noun_count.items():

            print(key, value)

    except FileNotFoundError as e:

        print(str(e))


if __name__ == "__main__":
    main()
