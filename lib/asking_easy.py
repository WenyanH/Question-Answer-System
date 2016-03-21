
def easy_question_generator(line):
	#collection
	col = ["is", "are", "am", "was", "were"]
	col_up = ["Is", "Are", "Am", "Was", "Were"]

	col_out = []
	line = line.strip()
	for i in range(len(col)):
		#if the sentence has the key words
		if col[i] in line:
			arr = line.split(" ")
			mark = -1
			#iterate each word
			for j in range(len(arr)):
				#determine whether number or alphabet
				if not arr[j].isalnum():
					#record the location of none-alnum
					mark = j 
					#print "mark + " + str(mark)
				if arr[j] == col[i]:
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
		
if __name__ == "__main__":
	print easy_question_generator("Guanxi is taking photos .")
	print easy_question_generator("Guanxi is not taking photos .")
	print easy_question_generator("Haha ni hao .")
