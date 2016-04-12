import string
def easy_question_generator(line_, position, upper_words):
	#collection delete "will"
	col = ["is", "are", "am", "was", "were", "can", "could", "must", "should", "may", "might", "would", "shall"]
	col_up = ["Is", "Are", "Am", "Was", "Were", "Can", "Could", "Must", "Should", "May", "Might", "Would", "Shall"]

	demon = ["it", "its", "this", "that", "those", "these", "me", "my", "mine", "we", "us", "our", "ours", "you", "your", "yours", "he", "him", "his", "she", "her", "hers","they", "them", "their", "theirs"]
	demon_up = ["It", "Its", "This", "That", "Those", "These", "Me", "My", "Mine", "We", "Us", "Our", "Ours", "You", "Your", "Yours", "He", "Him", "His", "She", "Her", "Hers", "They", "Them", "Their", "Theirs"]

	if position == 0:
		return None

	line = []
	for token in line_:
		line.append(token)

	col_out = []
	#line = line.strip()
	#arr = line.split(" ")
	mark = -1
	#determine whether ","
	for i in range(position):
		if line[i].orth_ == unicode(","):
			mark = i
	demon_status = False
	question_word = -1
	for i in range(mark + 1, position + 1):
		if line[i].orth_ in  demon or line[i].orth_ in demon_up:
			demon_status = True
			break
		elif line[i].orth_ in col:
			question_word = i;
	if demon_status == True or question_word == -1:
		return None
	#Special case:
	#Solve feature like "Someone, called A, is a boy"
	#print line
	#print "position" + str(position)
	#print "mark" + str(mark)
	if line[position - 1].pos_ == "VERB":
		position = position - 1
	if line[question_word - 1].orth_ == unicode(","):
		col_out.append(line[question_word].orth_.encode('utf8')[0].upper() + line[question_word].orth_.encode('utf8')[1: len(line[question_word].orth_)])


		#uppercase or lowercase for the first word
		if line[0].orth_ in upper_words:
			col_out.append(line[0].orth_.encode('utf8'))
		else:
			col_out.append(line[0].orth_.encode('utf8').lower())

		for i in range(1, len(line) - 1):
			if i == question_word:
				continue
			else:
				col_out.append(line[i].orth_.encode('utf8'))
		col_out.append("?")
		return ' '.join(col_out)


	for i in range(mark + 1):
		col_out.append(line[i].orth_.encode('utf8'))
	#print mark
	#print type(mark)

	#determine uppercase or lowercase
	#upper_lower = line[mark + 1].orth_.encode('utf8').lower()




	if (mark == -1):
		col_out.append(line[question_word].orth_.encode('utf8')[0].upper() + line[question_word].orth_.encode('utf8')[1: len(line[question_word].orth_)])
	else:
		col_out.append(line[question_word].orth_.encode('utf8'))

	for i in range(mark + 1, len(line) - 1):
		#determine uppercase or lowercase
		if i == (mark + 1):
			if line[mark + 1].orth_ in upper_words:
				col_out.append(line[mark + 1].orth_.encode('utf8'))
			else:
				col_out.append(line[mark + 1].orth_.encode('utf8').lower())


		#add question word
		elif i == question_word:
			continue
		else:
			col_out.append(line[i].orth_.encode('utf8'))
	col_out.append("?")
	#for m in col_out:
	#	print m,
	return ' '.join(col_out)



if __name__ == "__main__":
	#print easy_question_generator("Guanxi takes photos .", 1)
	print easy_question_generator("Guanxi can not taking photos when he is at home .", 2)
	print easy_question_generator("When he is at home , Guanxi can not taking photos .", 9)
	print easy_question_generator("Haha ni hao .", 3)
