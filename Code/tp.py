from nltk.corpus import stopwords

class Sentence_Scorer:

	def score(self,strong_synsets,lexical_chain,sentences,word_sentence):
		sentence_score = []

		#print(sentences)

		for sentence in sentences:
			
			sentence_score.append(0)

		unrepeated_strong_words = []
		for synset in strong_synsets:

			if(lexical_chain.__contains__(synset)):
				
				words_in_chain = lexical_chain[synset]

				for word in words_in_chain:
					if(not(word in unrepeated_strong_words)):
						unrepeated_strong_words.append(word)
					

		print(unrepeated_strong_words)

		for word in unrepeated_strong_words:	

			sentences_word_appears_in = word_sentence[word]

			for sentence_number in sentences_word_appears_in:

				sentence_score[sentence_number - 1] = sentence_score[sentence_number - 1] + 1


		stops = set(stopwords.words("english"))
		j = 0
		total_score = 0
		for sentence in sentences:
			sentence_length = 0
			words = sentence.split()
			for word in words:
				if word.lower() not in stops:
					sentence_length = sentence_length + 1

			sentence_score[j] = sentence_score[j]/sentence_length
			
			total_score = total_score + sentence_score[j]			
			j = j + 1

		average_score = total_score/len(sentences)
		j = 0
		for sentence in sentences:
			
			if sentence_score[j] >= average_score:
				print(sentence + " ")

			j = j + 1

		return sentence_score

