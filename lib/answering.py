import heapq, sys
import math
from match_sentence import match_sentence

def answer_what(question, sentence_list):
	best_answer = None
	best_answer_prob = 0.0
	for sent in sentence_list:
		this_answer, this_prob = _answer_what(question, sent)
		if this_prob > best_answer_prob:
			best_answer = this_answer
			best_answer_prob = this_prob
	return best_answer

def _answer_what(question, sentence):
	# find chunks that is not in question
	possible_answer = []
	question_string = get_string_of_sent(question)
	for chunk in sentence.noun_chunks:
		if chunk.text not in question_string:
			possible_answer.append(chunk)

	# find head token of each candidates
	parent_answer_head = {}
	for chunk in possible_answer:
		head = chunk.root.head
		while head in question:
			parent_answer_head[head] = chunk

	# get the most possible candidate
	result_head = find_shallowest_token(sentence, parent_answer_head.keys())
	result_chunk = parent_answer_head[result_head]

	# calc the probabilty of this answer
	num_child_of_head = 0
	for node in result_head.children:
		if node in question:
			num_child_of_head += 1
	prob = float(num_child_of_head) / len(list(result_head.children))

	return result_chunk, prob

def find_shallowest_token(doc, token_list):
	nodes = [doc.sents.next().root]
	while len(nodes) != 0:
		temp = nodes.pop(0)
		if temp in token_list:
			return temp
		for child in temp.children:
			nodes.append(child)

def get_string_of_sent(sent):
    return ' '.join([token.orth_ for token in sent])


def answer_yesno(question, sentence_list):
	negative_words= []
	dic_antonyms = {}
	dic_synonyms = {}
	f = open("data/negative_word_library.txt", "r")
	for item in f.readlines():
		negative_words.append(item)
	f = open("data/antonyms.txt", "r")
	for item in f.readlines():
		arr = item.split(" ")
		dic_antonyms[arr[0]] = arr[1]
		dic_antonyms[arr[1]] = arr[0]
	f = open("data/synonyms.txt", "r")
	for item in f.readlines():
		arr = item.split(" ")
		dic_synonyms[arr[0]] = arr[1]
		dic_synonyms[arr[1]] = arr[0]

	index = 0
	min_dis, min_align = match_sentence([word.orth_ for word in question], [word.orth_ for word in sentence_list[0]])

	for i in range(1, 3):
		dis, align = match_sentence([word.orth_ for word in question], [word.orth_ for word in sentence_list[i]])
		if min_dis > dis:
			min_dis = dis
			index = i
			min_align = align

	question_sign = 0
	sentence_sign = 0
	antonyms = False

	for item in align:
		arr = item.split(',')
		if (int(arr[0]) != -1) and (int(arr[1]) != -1):
			# find antonyms
			#!!!original form
			if question[int(arr[0])].lemma_ in dic_synonyms and dic_synonyms.get(question[int(arr[0])].lemma_) == sentence_list[index][int(arr[1])].lemma_:
				antonyms = True
			# find synonyms
			elif question[int(arr[0])].lemma_ in dic_antonyms and dic_antonyms.get(question[int(arr[0])].lemma_) == sentence_list[index][int(arr[1])].lemma_:
				continue
			else:
				print "answer: NO"
				return "NO"
		# -1 condition find negative words
		else:

			#orignial form
			if (int(arr[0]) == -1) and sentence_list[index][int(arr[1])].lemma_ in negative_words:
				sentence_sign = sentence_sign + 1
			elif (int(arr[1]) == -1) and question[int(arr[0])].lemma_ in negative_words:
				question_sign = question_sign + 1

	if antonyms == True:
		question_sign = question_sign + 1
	if (question_sign % 2) == (sentence_sign % 2):
		print "answer: YES"
		return "YES"
	else:
		print "answer: NO"
		return "NO"


	f.close()

def find_possible_sentences(docs, question):
	potential_sentences_index = []
	heap = []
	total_number_sentence = len(docs)
	#print total_number_sentence
	for sent in docs:
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
			weight_temp = frequency_in_sentence[token.lemma_] * math.log(total_number_sentence / count)
			for token_question in question:
				if token_question.lemma_ == token.lemma_:
					if token.lemma_ in exist_token:
						continue
					else:
						weight += weight_temp
						exist_token[token.lemma_] = 1
		#print weight
		heapq.heappush(heap, (weight * -1, docs.index(sent)))

	for i in range(3):
		potential_sentences_index.append(heapq.heappop(heap)[1])
	return potential_sentences_index

	# @param
	# 	texts: 2-d array of all sentences (after tokened)
	# 	question: string
	# 	quesiton_tags: 1-d of tags of question
	# @return
	#	1-d array of index in texts
	#  tags = {ADJ, ADP, ADV, AUX, CONJ, DET, INTJ, NOUN, NUM, PART, PRON, PROPN, PUNCT, SCONJ, SYM, VERB, X, EOL, SPACE}
	# weight = 0
	# heap = []
	# potential_sentences_index = []
	# question_tokens = question.split(" ")
	# for i in range(len(texts)):
	# 	weight = 0.0
	# 	for j in range(len(question_tags)):
	# 		if question_tags[j] == 'NOUN':
	# 			for k in range(len(texts[i])):
	# 				if question_tokens[j] == texts[i][k]:
	# 					weight = weight + 1
	# 		if question_tags[j] == 'ADJ':
	# 			for k in range(len(texts[i])):
	# 				if question_tokens[j] == texts[i][k]:
	# 					weight = weight + 0.5
	# 		if question_tags[j] == 'ADV':
	# 			for k in range(len(texts[i])):
	# 				if question_tokens[j] == texts[i][k]:
	# 					weight = weight + 0.3
	# 	heapq.heappush(heap, (weight*-1, i))
	# for i in range(3):
	# 	potential_sentences_index.append(heapq.heappop(heap)[1])
	# return potential_sentences_index

if __name__ == "__main__":
	question = "Is John a handsome and stubborn teacher ?"
	question_tags = ['VERB', 'NOUN', 'DET', 'ADJ', 'XXX', 'ADJ', 'NOUN', 'DSA']
	text = [['John', 'is', 'a', 'handsome', 'director'], ['John', 'likes', 'Ravi'], ['John', 'is', 'a', 'handsome', 'and', 'stubborn', 'teacher', '.']]
	print(find_possible_sentences(text, question, question_tags))
