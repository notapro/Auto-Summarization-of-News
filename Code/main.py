'''
Created on Feb 21, 2016

@author: Sameer
'''
from Code.Tokenizer import Tokenizer


def main():
    
    input_file = "../Input Files/InputFile1.txt"
    
    tokenizer_object = Tokenizer()
    
    tokenizer_object.extract_words(input_file)
    
    
    

if __name__ == "__main__": main()
    