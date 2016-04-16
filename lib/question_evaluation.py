import math
import heapq

def question_evalution(question_doc_list, wiki_doc_list, n):
	heap = []
	final_questions = []
	demon = ['i', 'I', "it", "its", "this", "that", "those", "these", "me", "my", "mine", "we", "us", "our", "ours", "you", "your", "yours", "he", "him", "his", "she", "her", "hers","they", "them", "their", "theirs"]
	total_number_questions = len(wiki_doc_list)
	for sent in question_doc_list:
		number_of_words = len(sent)
		if number_of_words <= 6:
			continue
		weight = 0
		frequency_in_sentence = {}
		exist_token = {}
		for token in sent:
			if token.lemma_ in frequency_in_sentence:
				frequency_in_sentence[token.lemma_] += 1
			else:
				frequency_in_sentence[token.lemma_] = 1
		for token in sent:
			if token in demon:
				break
			count = 0
			for sent2 in wiki_doc_list:
				for token2 in sent2:
					if token2.lemma_ == token.lemma_:
						count = count + 1
						break
			if count == 0:
				weight_temp = 0
			else:
				weight_temp = frequency_in_sentence[token.lemma_] * math.log(total_number_questions / count)
			weight += weight_temp
		#print weight
		weight = weight / (number_of_words**2)
		s = ''
		for word in sent:
			s += word.orth_ + ' '
		s = s.rstrip()
		heapq.heappush(heap, (weight * -1, s))

	for i in range(n):
		final_questions.append(heapq.heappop(heap)[1])
	return final_questions

if __name__ == "__main__":
	pass
