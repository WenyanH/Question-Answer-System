# from lib import helper

def hard_question_generator(line):
	fin = open('data/antonyms.txt', 'r')
	antonyms1 = []
	antonyms2 = []
	for pairs in fin:
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
		return s 

    # 1. check if line can be a hard questions
    # 2. xxx
    # return None if False
    # replace
    # line = helper.convert_declarative_to_question(line)
    # return line


if __name__ == '__main__':
	sentence = 'Xichen is ugly and tall .'
	print(sentence)
	print(hard_question_generator(sentence))
