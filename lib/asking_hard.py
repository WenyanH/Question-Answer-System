import asking_easy
import random

def generate_special(line):
	words = line.split(" ")
	# hard_code for either... or ...
	flag_either_or = False
	if 'either' and 'or' in words:
		flag_either_or = True
		words[words.index('either')] = 'neither'
		words[words.index('or')] = 'nor'
	if flag_either_or == True:
		s = ''
		for word in words:
			s+= word + ' '
		return asking_easy.easy_question_generator(s)

	# hard_code for neither... nor ...
	flag_neither_nor = False
	if 'neither' and 'nor' in words:
		flag_neither_nor = True
		words[words.index('neither')] = 'either'
		words[words.index('nor')] = 'or'
	if flag_neither_nor == True:
		s = ''
		for word in words:
			s+= word + ' '
		return asking_easy.easy_question_generator(s)


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
	sentence = 'Xichen is neither fat nor tall .'
	print(sentence)
	print(generate_special(sentence))
