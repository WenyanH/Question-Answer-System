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
	print 'Q:'
	for word in question:
		print word.orth_, '(' + word.pos_ + ')',
	print

	for sen in sentence_list:
		print 'S:'
		for word in sen:
			print word.orth_, '(' + word.pos_ + ')',
		print

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
