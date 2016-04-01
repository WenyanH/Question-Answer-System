import heapq, sys

def answer_what(question, sentence_list, noun_chunks_list):
	print 'Q:'
	for word in question:
		print word.orth_, '(' + word.pos_ + ')',
	print

	for sen, chunks in zip(sentence_list, noun_chunks_list):
		print 'S:'
		for word in sen:
			print word.orth_, '(' + word.pos_ + ')',
		print
		print 'Chunks:', chunks


def answer_yesno(question, sentence_list):
	'''
	print 'Q:'
	for word in question:
		print word.orth_, '(' + word.pos_ + ')',
	print

	for sen in sentence_list:
		print 'S:'
		for word in sen:
			print word.orth_, '(' + word.pos_ + ')',
		print
	'''
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
    	
	'''
	question_pos = [word.pos_ for word in question]
	question_orth = [word.orth_ for word in question]
	sentence0_pos = [word.pos_ for word in sentence_list[0]]
	sentence0_orth = [word.orth_ for word in sentence_list[0]]
	sentence1_pos = [word.pos_ for word in sentence_list[1]]
	sentence1_orth = [word.orth_ for word in sentence_list[1]]
	sentence2_pos = [word.pos_ for word in sentence_list[2]]
	sentence2_orth = [word.orth_ for word in sentence_list[2]]
	'''


	index = 0
	min_dis, min_align = match_sentence([word.orth_ for word in question], [word.orth_ for word in sentence_list[0]])
	
	for i in range(1, 3):
		dis, align = match_sentence([word.orth_ for word in question], [word.orth_ for word in "sentence_list[" + str(i) + "]"])
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
			else
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
	
def find_possible_sentences(doc, question):
	for sent in doc.sents:
		for token in sent:
			print token.orth_, token.pos_, token.lemma_
		print

	for token in question:
		print token.orth_, token.pos_, token.lemma_


	sys.exit(0)
	# @param
	# 	texts: 2-d array of all sentences (after tokened)
	# 	question: string
	# 	quesiton_tags: 1-d of tags of question
	# @return
	#	1-d array of index in texts
	#  tags = {ADJ, ADP, ADV, AUX, CONJ, DET, INTJ, NOUN, NUM, PART, PRON, PROPN, PUNCT, SCONJ, SYM, VERB, X, EOL, SPACE}
	weight = 0
	heap = []
	potential_sentences_index = []
	question_tokens = question.split(" ")
	for i in range(len(texts)):
		weight = 0.0
		for j in range(len(question_tags)):
			if question_tags[j] == 'NOUN':
				for k in range(len(texts[i])):
					if question_tokens[j] == texts[i][k]:
						weight = weight + 1
			if question_tags[j] == 'ADJ':
				for k in range(len(texts[i])):
					if question_tokens[j] == texts[i][k]:
						weight = weight + 0.5
			if question_tags[j] == 'ADV':
				for k in range(len(texts[i])):
					if question_tokens[j] == texts[i][k]:
						weight = weight + 0.3
		heapq.heappush(heap, (weight*-1, i))
	for i in range(3):
		potential_sentences_index.append(heapq.heappop(heap)[1])
	return potential_sentences_index

if __name__ == "__main__":
	question = "Is John a handsome and stubborn teacher ?"
	question_tags = ['VERB', 'NOUN', 'DET', 'ADJ', 'XXX', 'ADJ', 'NOUN', 'DSA']
	text = [['John', 'is', 'a', 'handsome', 'director'], ['John', 'likes', 'Ravi'], ['John', 'is', 'a', 'handsome', 'and', 'stubborn', 'teacher', '.']]
	print(find_possible_sentences(text, question, question_tags))
