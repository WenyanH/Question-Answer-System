from recursion import recursion

def match_sentence(sentence1, sentence2):
	#sentence1, sentence1_tag, sentence2_tag and sentence2 are arrays
	#print "sentence1:"
	#print sentence1
	#print "sentence2:"
	#print sentence2

	max_row = len(sentence1)
	max_col = len(sentence2)
	#print str(max_col) + " ======" + str(max_row)
	#create a two-dimensional array to record the Levenshtein distance
	memo = [[0 for col in range(max_col + 1)] for row in range(max_row + 1)]
	#initialize the two-dimensional array
	for i in range(max_row + 1):
		memo[i][0] = i
	for i in range(max_col + 1):
		memo[0][i] = i

	for j in range(1, max_col + 1):
		for k in range(1, max_row + 1):
			if cmp(sentence2[j - 1], sentence1[k - 1]) == 0:
				memo[k][j] = min(memo[k - 1][j] + 1, memo[k][j - 1] + 1)
				memo[k][j] = min(memo[k][j], memo[k - 1][j - 1])
			else:
				memo[k][j] = min(memo[k - 1][j] + 1, memo[k][j - 1] + 1)
				memo[k][j] = min(memo[k][j], memo[k - 1][j - 1] + 1)
	#print "matrix: " + str(memo[max_row][max_col])

	'''
	for i in range(len(memo)):
		for j in range(len(memo[0])):
			print str(memo[i][j]) + "   ",
		print
	'''

	row_coll = []
	col_coll = []
	row_index = len(memo) - 1
	col_index = len(memo[0]) - 1
	direc = []
	recursion(memo, row_coll, col_coll, row_index, col_index, direc)
	#print direc
	'''
	print "row_coll  " + str(row_coll)
	print "col_coll  " + str(col_coll)
	print direc
	'''
	'''
	for i in range(len(memo)):
		for j in range(len(memo[0])):
			print str(memo[i][j]) + "    ",
		print
	'''

	#former: sentence1; later: sentence2
	align = []
	#i: sentence1; j: sentence2
	for i in range(len(direc)):
		if (direc[i] == "transpose") and (sentence1[row_coll[i] - 1] == sentence2[col_coll[i] - 1]):
			continue
		elif (direc[i] == "transpose") and  (not (sentence1[row_coll[i] - 1] == sentence2[col_coll[i] - 1])):
			align.append(str(row_coll[i] - 1) + "," + str(col_coll[i] - 1))
		elif (direc[i] == "up"):
			align.append(str(row_coll[i] - 1) + "," + str(-1))
		else:
			align.append(str(-1) + "," + str(col_coll[i] - 1))
	#print align
	'''
	print "row_coll"
	print row_coll
	print "col_coll"
	print col_coll
	'''
	align_up = []
	align_down = []
	for i in range(len(align)):
		#print "align[i]= " + align[i]
		arr = align[i].split(",")
		align_up.append(int(arr[0]))
		align_down.append(int(arr[1]))
	#print align_up
	#print align_down



	#count the number of unalignments
	count = 0
	for i in range(len(align_up)):
		if align_up[i] == -1:
			if (i > 0) and (align_down[i - 1] + 1 == align_down[i]) and (align_up[i - 1] == -1):
				#print "align_up[i] == -1 && match && i + count: " + str(i) + str(count)
				continue
			else:
				#print "align_up[i] == -1 && not match && i + count: " + str(i) + str(count)
				count = count + 1
		elif align_down[i] == -1:
			if (i > 0) and (align_up[i - 1] + 1 == align_up[i]) and (align_down[i - 1] == -1):
				#print "align_down[i] == -1 && match && i + count: " + str(i) + str(count)
				continue
			else:
				#print "align_dwon[i] == -1 && not match && i + count: " + str(i) + str(count)
				count = count + 1
		else:
			#print "transpose && i + count: " + str(i) + str(count)
			count = count + 1
	#print "count:" + str(count) 



	#print "finish-------------"

	#analyze conditions of transposition
	return count, align


	#analyze conditions of addition and deletion





	#return align











if __name__ == "__main__":
	#match_sentence(["when", "I", "go", "to", "school", "you", "are", "so", "beautiful"], ["you", "are", "so", "beautiful", "time"], ["you", "are", "so", "beautiful"], ["pron", "deter", "noun", "time"])
	match_sentence(["when", "I", "go", "to", "school", "you", "are", "so", "beautiful"], ["you", "are", "so", "beautiful"])
	#match_sentence(["you", "are", "so", "beautiful", "when", "I", "go", "to", "school"], ["you", "are", "so", "beautiful", "time"], ["you", "are", "so", "beautiful"], ["pron", "deter", "noun", "time"])
	match_sentence(["you", "are", "so", "beautiful", "when", "I", "go", "to", "school"], ["you", "are", "so", "beautiful"])
	#match_sentence(["in", "fact", ",", "you", "are", "so", "beautiful", "when", "I", "go", "to", "school"], ["you", "are", "so", "beautiful", "time"], ["in", "fact", ",", "I", "am", "a", "good", "student", "and", "a", "good", "man"], ["pron", "deter", "noun", "time"])
	match_sentence(["in", "fact", ",", "you", "are", "so", "beautiful", "when", "I", "go", "to", "school"], ["in", "fact", ",", "I", "am", "a", "good", "student", "and", "a", "good", "man"])
	#match_sentence(["in", "fact", ",", "you", "are", "so", "beautiful", "when", "I", "go", "to", "school"], ["you", "are", "so", "beautiful", "time"], ["in", "fact", ",", "I", "am", "a", "good", "student"], ["pron", "deter", "noun", "time"])
	#match_sentence(["a", "b", ",", "you", "are", "so", "beautiful", "when", "I", "go", "to", "school"], ["you", "are", "so", "beautiful", "time"], ["in", "fact", ",", "I", "am"], ["pron", "deter", "noun", "time"])
	#match_sentence(["But", "spanish", "the", "official", "or", "national", "language", "in", "Spain", ",", "Equatorial", "Guinea", ",", "and", "19", "countries", "in", "the", "Americas"], [], ["spanish", "the", "official", "or", "national", "language", "in", "Spain", ",", "Equatorial", "Guinea", ",", "and", "19", "countries", "in", "the", "Americas"], [])
	match_sentence(["in", "fact", ",", "you", "are", "so", "beautiful", "when", "I", "go", "to", "school"], ["in", "fact", ",", "I", "am", "a", "good", "student"])
	match_sentence(["a", "b", ",", "you", "are", "so", "beautiful", "when", "I", "go", "to", "school"], ["in", "fact", ",", "I", "am"])
	match_sentence(["But", "spanish", "the", "official", "or", "national", "language", "in", "Spain", ",", "Equatorial", "Guinea", ",", "and", "19", "countries", "in", "the", "Americas"], ["spanish", "the", "official", "or", "national", "language", "in", "Spain", ",", "Equatorial", "Guinea", ",", "and", "19", "countries", "in", "the", "Americas"])
