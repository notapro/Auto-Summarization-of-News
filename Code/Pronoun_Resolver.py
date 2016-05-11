__author__ = 'pro'

from pycorenlp import StanfordCoreNLP
from nltk.tokenize import word_tokenize, sent_tokenize


class Pronoun_Resolver:

    def resolve(self, text):

        sentences_all = sent_tokenize(text, 'English')

        for i in range(2, len(sentences_all)):
            text2 = sentences_all[i-2]+' '+sentences_all[i-1]+' '+sentences_all[i]
            print(text2)
            sentences = sent_tokenize(text2, 'English')
            print(sentences)
            nlp = StanfordCoreNLP('http://localhost:9000')
            output = nlp.annotate(text2, properties={
                'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,mention,dcoref',
                'outputFormat': 'json'
            })

            # target.write(output)
            # target.close()
            corefs = output['corefs']
            cnt = 1

            for key, chains in corefs.items():

                substitute = ''
                print("\nchain number "+str(cnt))
                cnt += 1
                for chain in chains:

                    # print(chain['isRepresentativeMention']+'\n')
                    print(chain['type'] + ' ' + chain['text'])
                    if (chain['isRepresentativeMention'] is True) and (chain['type'] != 'PRONOMINAL'):
                        substitute = str(chain['text'])
                        print(substitute+'\n')

                    if (chain['type'] == 'PRONOMINAL') and (substitute != ''):
                        sentence_num = chain['sentNum']
                        words = word_tokenize(sentences[sentence_num - 1], 'English')
                        words[chain['startIndex'] - 1] = substitute
                        new_sentence = ' '.join(words)
                        sentences[sentence_num - 1] = new_sentence

            sentences_all[i-2] = sentences[0]
            sentences_all[i-1] = sentences[1]
            sentences_all[i] = sentences[2]

        return sentences_all




