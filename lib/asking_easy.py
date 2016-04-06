import string
def easy_question_generator(line, position):
	#collection
	col = ["is", "are", "am", "was", "were", "can", "could", "must", "should", "may", "might", "will", "would", "shall"]
	col_up = ["Is", "Are", "Am", "Was", "Were", "Can", "Could", "Must", "Should", "May", "Might", "Will", "Would", "Shall"]

	demon = ["it", "its", "this", "that", "those", "these"]
	demon_up = ["It", "Its", "This", "That", "Those", "These"]

	if position == 0:
		return None

	col_out = []
	line = line.strip()
	arr = line.split(" ")
	mark = -1
	#determine whether number or alphabet
	for i in range(position):
		sign = False
		for m in range(len(arr[i])):
			if arr[i].strip()[m] in string.ascii_letters or arr[i].strip()[m] in string.digits:
				sign = True
				break
		#record the location of none-alnum
		if sign == False:
			mark = i
	question_word = -1
	for i in range(mark + 1, position + 1):
		if i > 0 and arr[i] in col and arr[i - 1] not in demon and arr[i - 1] not in demon_up:
			question_word = i;
			break;
	if question_word == -1:
		return None
	for i in range(mark + 1):
		col_out.append(arr[i])
	#print mark
	#print type(mark)
	arr[mark + 1] = arr[mark + 1].lower()
	if (mark == -1):
		col_out.append(arr[question_word][0].upper() + arr[question_word][1: len(arr[question_word])])
	else:
		col_out.append(arr[question_word])

	for i in range(mark + 1, len(arr) - 1):
		if i == question_word:
			continue
		else:
			col_out.append(arr[i])
	col_out.append("?")
	#for m in col_out:
	#	print m,
	return ' '.join(col_out)

	'''
	for i in range(len(col)):
		#if the sentence has the key words
		if col[i] in line:
			arr = line.split(" ")
			mark = -1
			#iterate each word
			for j in range(len(arr)):
				#determine whether number or alphabet
				sign = False
				for m in range(len(arr[j])):
					if arr[j].strip()[m] in string.ascii_letters or arr[j].strip()[m] in string.digits:
						sign = True
						break
					#record the location of none-alnum
				if sign == False:
					mark = j
		


				#if not arr[j].isalnum():
					#record the location of none-alnum
				#	mark = j 
					#print "mark + " + str(mark)
				if arr[j] == col[i]:
					if j > 0 and (arr[j - 1] in demon or arr[j - 1] in demon_up):
						break
					#print "being + " + str(j)
					if not (mark + 1) == j:	
						#print "match + " + str(j)
						#insert words that is before the key word
						for jj in range(mark + 1):
							col_out.append(arr[jj])
						#insert the key word
						#if mark == -1, there is no clause
						if mark == -1:	
							col_out.append(col_up[i])
						else:
							col_out.append(col[i])
						for k in range(mark + 1, len(arr)):
						#continue if it is the key word itself
							if k == j:
								continue;
							#if it is the first word, lowercase	
							elif k == (mark + 1):
								f_letter = arr[mark + 1].lower()
								col_out.append(f_letter)
							#change the last symbol to "?"	
							elif k == (len(arr) - 1):
								col_out.append("?"),
							else:
								col_out.append(arr[k])
					else: 
						col_out.append(col_up[i])
						for k in range(len(arr)):
						#continue if it is the key word itself
							if k == j:
								continue;
							#if it is the first word, lowercase	
							elif k == 0:
								f_letter = arr[0].lower()
								col_out.append(f_letter)
							#change the last symbol to "?"	
							elif k == (len(arr) - 1):
								col_out.append("?"),
							else:
								col_out.append(arr[k])
					#output
					#for m in col_out:
					#	print m,
					return ' '.join(col_out)
					#print ""	
					#print "finish ------------------"
					break;
			break;		
		else:
			continue;
	'''
		
if __name__ == "__main__":
	#print easy_question_generator("Guanxi takes photos .", 1)
	print easy_question_generator("Guanxi can not taking photos when he is at home .", 2)
	print easy_question_generator("When he is at home , Guanxi can not taking photos .", 9)
	print easy_question_generator("Haha ni hao .", 3)
