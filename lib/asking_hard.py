import asking_easy
import random


def generate_antonyms(line):
	fin_antonyms = open('data/antonyms.txt', 'r')
	antonyms1 = []
	antonyms2 = []
	for pairs in fin_antonyms:
		pairs = pairs.rstrip()
		words = pairs.split(" ")
		antonyms1.append(words[0])
		antonyms2.append(words[1])
	words = line.split(" ")
	flag = False
	for i in range(len(words)):
		if words[i] in antonyms1:
			flag = True
			words[i] = antonyms2[antonyms1.index(words[i])]
			break
	if flag == False:
		return None
	else:
		s = ''
		for word in words:
			s += word + ' '
		return asking_easy.easy_question_generator(s)

def generate_synonyms(line):
	fin_synonyms = open('data/synonyms.txt', 'r')
	synonyms1 = []
	synonyms2 = []
	for pairs in fin_synonyms:
		pairs = pairs.rstrip()
		words = pairs.split(" ")
		synonyms1.append(words[0])
		synonyms2.append(words[1])
	words = line.split(" ")
	flag = False
	for i in range(len(words)):
		if words[i] in synonyms1:
			flag = True
			words[i] = synonyms2[synonyms1.index(words[i])]
			break
	if flag == False:
		return None
	else:
		s = ''
		for word in words:
			s += word + ' '
		return asking_easy.easy_question_generator(s)


def hard_question_generator(line):
	ran_num = random.random()
	if ran_num < 0.5:
		return generate_antonyms(line)
	else:
		return generate_synonyms(line)


    # 1. check if line can be a hard questions
    # 2. xxx
    # return None if False
    # replace
    # line = helper.convert_declarative_to_question(line)
    # return line


if __name__ == '__main__':
	sentence = 'Xichen is fat and tall .'
	print(sentence)
	print(hard_question_generator(sentence))
