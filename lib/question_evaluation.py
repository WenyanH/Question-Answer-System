import math
import heapq

def question_evalution(question_list):
	heap = []
	total_number_questions = len(question_list)
	for sent in question_list:
		number_of_words = len(sent)
		weight = 0
		frequency_in_sentence = {}
		exist_token = {}
		for token in sent:
			if token.lemma_ in frequency_in_sentence:
				frequency_in_sentence[token.lemma_] += 1
			else:
				frequency_in_sentence[token.lemma_] = 1
		for token in sent:
			count = 0
			for sent2 in docs:
				for token2 in sent2:
					if token2.lemma_ == token.lemma_:
						count = count + 1
						break
			weight_temp = frequency_in_sentence[token.lemma_] * math.log(total_number_questions / count)
			for token_question in question:
				if token_question.lemma_ == token.lemma_:
					if token.lemma_ in exist_token:
						continue
					else:
						weight += weight_temp
						exist_token[token.lemma_] = 1
		#print weight
		weight = weight / number_of_words
		s = ''
		for word in sent:
			s += word + ' '
		s = s.rstrip()
		s = s + '?'
		heapq.heappush(heap, (weight * -1, s))

if __name__ == "__main__":
	