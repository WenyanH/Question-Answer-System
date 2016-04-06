import heapq, sys
import math
from match_sentence import match_sentence
from abbre_align import abbre_align

def answer_why(question, sentence_list, sentence_prob):
	keywords = ['because', 'due to']
	for sent in sentence_list:
		for k_word in keywords:
			if k_word in get_string_of_sent(sent).lower():
				# print k_word
				result =  _answer_why(sent, k_word)
				if result:
					return result
	return answer_what(question, sentence_list, sentence_prob)

def _answer_why(sentence, keyword):
	keyword = keyword.split(' ')[0]
	tree_root = None
	for token in sentence:
		if token.orth_.lower() == keyword:
			tree_root = token.head
			break
	else:
		return None

	result = ""
	for token in tree_root.subtree:
		result += token.orth_ + ' '
	return result

def answer_what(question, sentence_list, sentence_prob):
	best_answer = None
	best_answer_prob = 0.0
	for index, sent in enumerate(sentence_list):
		this_answer, this_prob = _answer_what(question, sent)
		# print this_prob, sentence_prob[index], '->', this_prob * sentence_prob[index]
		if this_prob * sentence_prob[index] > best_answer_prob:
			best_answer = this_answer
			best_answer_prob = this_prob * sentence_prob[index]
	return best_answer

def answer_when(question, sentence_list, sentence_prob):
	for sent in sentence_list:
		result = _answer_by_entity(question, sent, ['DATE', 'TIME'])
		if result != None:
			return result
	return get_string_of_sent(sentence_list[0])

def answer_who(question, sentence_list, sentence_prob):
	for sent in sentence_list:
		result = _answer_by_entity(question, sent, ['PERSON'])
		if result != None:
			return result
	return get_string_of_sent(sentence_list[0])

def answer_where(question, sentence_list, sentence_prob):
	for sent in sentence_list:
		result = _answer_by_entity(question, sent, ['GPE', 'LOC', 'ORG', 'FACILITY'])
		if result != None:
			return result
	return get_string_of_sent(sentence_list[0])

def answer_how_something(question, sentence_list, sentence_prob, question_type):
	entities = []
	if question_type == 'HOW LONG':
		entities = ['QUANTITY']
	elif question_type == 'HOW MUCH':
		entities = ['MONEY']
	else:
		entities = ['CARDINAL']

	for sent in sentence_list:
		result = _answer_by_entity(question, sent, entities)
		if result != None:
			return get_string_of_sent(result)
	return get_string_of_sent(sentence_list[0])

def _answer_by_entity(question, sentence, ent_list):
	for chunk in sentence.ents:
		if chunk.label_ in ent_list and \
			chunk.orth_.lower() not in get_string_of_sent(question).lower():
			return chunk
	return None

def answer_how(question, sentence_list, sentence_prob):
	keywords = ['by']
	for sent in sentence_list:
		for k_word in keywords:
			if k_word in get_string_of_sent(sent).lower():
				# print k_word
				result =  _answer_how(sent, k_word)
				if result:
					return result
	return answer_what(question, sentence_list, sentence_prob)

def _answer_how(sentence, keyword):
	keyword = keyword.split(' ')[0]
	tree_root = None
	for token in sentence:
		if token.orth_.lower() == keyword:
			tree_root = token.head
			break
	else:
		return None

	result = ""
	for token in tree_root.subtree:
		result += token.orth_ + ' '
	return result

def _answer_what(question, sentence):
	# find chunks that is not in question
	possible_answer = []
	question_string = get_string_of_sent(question).lower()
	for chunk in sentence.noun_chunks:
		# print chunk, chunk.label_
		if chunk.text.lower() not in question_string:
			possible_answer.append(chunk)
	for chunk in sentence.ents:
		# print chunk, chunk.label_
		if chunk.text.lower() not in question_string:
			possible_answer.append(chunk)

	# find head token of each candidates
	parent_answer_head = {}
	for chunk in possible_answer:
		head = chunk.root.head
		while head.text not in get_string_of_sent(question):
			if head.head is head:
				break
			head = head.head
		parent_answer_head[head] = chunk

	# get the most possible candidate
	result_head = find_shallowest_token(sentence, parent_answer_head.keys())
	result_chunk = parent_answer_head[result_head]

	# calc the probabilty of this answer
	num_child_of_head = 1
	for node in result_head.children:
		if node.text in get_string_of_sent(question):
			num_child_of_head += 1
	prob = float(num_child_of_head) / (len(list(result_head.children)) + 1)

	if prob > 0.3:
		return get_string_of_sent(result_chunk), prob
	else:
		return get_string_of_sent(sentence), prob

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


def answer_yesno(question_old, sentence_list_old):
	#preprocess
	#lowercase, delete "BE"
	#print sentence_list_old

	delete_word = ["it", "be", "do", "can", "could", "will", "would", "need","should", "must", "shall", "may", "might", "the", "of", "a", "an", "anyone", "anything", "to"]
	#not should can do did does!!!
	question = []
	sentence_list = []
	sentence_one = []
	for word in question_old:
		#if (not word.lemma_ == "it") and (not word.lemma_ == "be") and (not word.lemma_ == "do") and (not word.lemma_ == "can") and (not word.is_punct):
		if (not word.lemma_.lower() in delete_word) and (not word.is_punct):
			question.append(word)
	print "question"
	print question
	for sentence in sentence_list_old:
		#print "sentence"
		#print sentence
		#print
		for word in sentence:
			#if (not word.lemma_ == "it") and (not word.lemma_ == "be") and (not word.lemma_ == "do") and (not word.lemma_ == "can") and (not word.is_punct):
			if (not word.lemma_.lower() in delete_word) and (not word.is_punct):
				sentence_one.append(word)
		print "sentence"
		print sentence_one
		sentence_list.append(sentence_one)
		sentence_one = []
	#print sentence_list


	negative_words= []
	dic_antonyms = {}
	dic_synonyms = {}
	f = open("data/negative_word_library.txt", "r")
	for item in f.readlines():
		#print item
		negative_words.append(item.strip())

	#type: unicode
	f = open("data/antonyms.txt", "r")
	for item in f.readlines():
		arr = item.split(" ")
		dic_antonyms[unicode(arr[0].strip().lower())] = unicode(arr[1].strip().lower())
		#dic_antonyms[arr[1]] = arr[0]
	f = open("data/synonyms.txt", "r")
	for item in f.readlines():
		arr = item.split(" ")
		dic_synonyms[unicode(arr[0].strip().lower())] = unicode(arr[1].strip().lower())
		#dic_synonyms[arr[1]] = arr[0]

	index = 0
	min_dis, min_align = match_sentence([word.lemma_.lower() for word in question], [word.lemma_.lower() for word in sentence_list[0]])
	#print "index" + str(index)

	for i in range(1, 3):
		dis, align = match_sentence([word.lemma_.lower() for word in question], [word.lemma_.lower() for word in sentence_list[i]])
		#print "dis:" + str(dis)
		if min_dis > dis:
			min_dis = dis
			index = i
			min_align = align
	#print "index" + str(index)
	print "before"
	print min_align
	print "index" + str(index)
	min_align = abbre_align(min_align)
	print "align"
	print min_align

	question_sign = 0
	sentence_sign = 0
	antonyms = False

	for item in min_align:
		arr = item.split(',')
		if (int(arr[0]) != -1) and (int(arr[1]) != -1):
			#print "1"
			# find antonyms
			#!!!original form
			if question[int(arr[0])].lemma_.lower() in dic_antonyms and dic_antonyms.get(question[int(arr[0])].lemma_.lower()) == sentence_list[index][int(arr[1])].lemma_.lower():
				#print "question[int(arr[0])].lemma_.lower():" + question[int(arr[0])].lemma_.lower()
				antonyms = True
			# find synonyms
			elif question[int(arr[0])].lemma_.lower() in dic_synonyms and dic_synonyms.get(question[int(arr[0])].lemma_.lower()) == sentence_list[index][int(arr[1])].lemma_.lower():
				continue
			else:
				#print question[int(arr[0])].lemma_.lower()
				return "NO"
		# -1 condition find negative words
		else:
			#not check clauses


			#orignial form
			if (int(arr[0]) == -1) and sentence_list[index][int(arr[1])].lemma_.lower() in negative_words:
				sentence_sign = sentence_sign + 1
			elif (int(arr[1]) == -1) and question[int(arr[0])].lemma_.lower() in negative_words:
				question_sign = question_sign + 1

	#print "question_sign:" + str(question_sign)
	#print "sentence_sign:" + str(sentence_sign)
	#print "antonyms:" + str(antonyms)

	if antonyms == True:
		question_sign = question_sign + 1
	if (question_sign % 2) == (sentence_sign % 2):
		return "YES"
	else:
		return "NO"

	f.close()

def find_possible_sentences(docs, question):
	potential_sentences_index = []
	potential_sentences_prob = []
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

	threshold = -1 * heap[0][0] / 100.0
	if threshold > 0.1:
		for i in range(3):
			pairs = heapq.heappop(heap)
			potential_sentences_index.append(pairs[1])
			potential_sentences_prob.append(-1 * pairs[0] / 100.0)
	else:
		for i in range(5):
			pairs = heapq.heappop(heap)
			potential_sentences_index.append(pairs[1])
			potential_sentences_prob.append(-1 * pairs[0] / 100.0)

	print potential_sentences_prob
	return potential_sentences_index, potential_sentences_prob

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
