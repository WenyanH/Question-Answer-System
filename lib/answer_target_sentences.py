import nltk
import heapq

def possbility_generate(sentence1, sentence2):
	weight = 0
	tokens1 = nltk.word_tokenize(sentence1)
	tokens2 = nltk.word_tokenize(sentence2)
	tagged_sentence1 = nltk.pos_tag(tokens1)
	for i in range(len(tokens1)):
		if tagged_sentence1[i][1] == 'NN' or tagged_sentence1[i][1] == 'NNS' or tagged_sentence1[i][1] == 'NNP' or tagged_sentence1[i][1] == 'NNPS':
			for word in tokens2:
				if tagged_sentence1[i][0] == word:
					weight = weight + 1
	return weight

def target_sentences(question, fulltext):
	heap = []
	potential_answers = []
	for sentence in fulltext:
		possbility_temp = possbility_generate(question, sentence)
		heapq.heappush(heap, (possbility_temp*-1, sentence))
	for i in range(3):
		potential_answers.append(heapq.heappop(heap)[1])
	return potential_answers

if __name__ == "__main__":
	# sen1 = "Is John a good teacher and a good husband ?"
	# sen2 = "John is a good teacher and a good husband ."
	# sen3 = "John is a stuborn teacher ."
	# sen4 = "John is handsome ."
	# sen5 = "John likes Ravi ."
	# sen = []
	# sen.append(sen2)
	# sen.append(sen3)
	# sen.append(sen4)
	# sen.append(sen5)
	#print(target_sentences(sen1, sen))
	que = "Is Spanish the official or national language in Spain, Equatorial Guinea, and 19 countries in the Americas ?"
	text = []
	fin = open('raw_data/data1.txt', 'r')
	for line in fin:
		if line != '\n':
			temp = line.decode('utf-8').strip()
			#print(line)
			text.append(temp.encode('ascii', 'ignore'))
	#print(text)
	print(target_sentences(que, text))

