
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
			#iterate each word
			for j in range(len(arr)):
				if arr[j] == col[i]:
					#insert the key word
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
					result = ""
					for m in col_out:
						result += m + " "
					return result
			break;
		else:
			continue;

if __name__ == "__main__":
	print easy_question_generator("Guanxi is taking photos .")
	print easy_question_generator("Guanxi is not taking photos .")
	print easy_question_generator("Haha ni hao .")
