from recursion import recursion

def match_sentence(sentence1, sentence2):
	#sentence1 and sentence2 are arrays
	#print len(sentence1)
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
	

	row_coll = []
	col_coll = []
	row_index = len(memo) - 1
	col_index = len(memo[0]) - 1
	direc = []
	recursion(memo, row_coll, col_coll, row_index, col_index, direc)	
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
	print align
	return align	


	#return memo[max_row][max_col]		



if __name__ == "__main__":
	match_sentence(["I", "am", "a", "aa", "student"], ["I", "not", "a"])
	match_sentence(["spanish", "the", "official", "or", "national", "language", "in", "Spain", ",", "Equatorial", "Guinea", ",", "and", "19", "countries", "in", "the", "Americas"], ["spanish", "the", "official", "or", "national", "language", "in", "Spain", ",", "Equatorial", "Guinea", ",", "and", "19", "countries", "in", "the", "Americas"])
	