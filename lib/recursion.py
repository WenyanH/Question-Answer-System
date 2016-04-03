import math

def recursion(memo, row_coll, col_coll, row_index, col_index, direc):
	#max_row = len(memo)
	#max_col = len(memo[0])
	if row_index == 0 and col_index == 0:
		return True
	if (row_index) < 0 or (col_index) < 0:
		return False
	#record the medium one	
	distance = []
	# 1: left up 
	# 2: right up
	# 3: left down
	if (row_index - 1 >= 0) and (col_index - 1 >= 0):
		distance.append(str(memo[row_index - 1][col_index - 1]) + "+" + "1")
	if (row_index - 1 >= 0):
		distance.append(str(memo[row_index - 1][col_index]) + "+" + "2")
	if col_index - 1 >= 0:
		distance.append(str(memo[row_index][col_index - 1]) + "+" + "3")
	
	for i in range(3):
		for j in range(i + 1, 3):
			if int(distance[i].split("+")[0]) > int(distance[j].split("+")[0]):
				temp = distance[i]
				distance[i] = distance[j]
				distance[j] = temp	
	#distance.sort()
	#mini = distance[0].split(",")[1]
	#medi = distance[1].split(",")[1]
	#maxi = distance[2].split(",")[1]
	'''
	print "row_index: " + str(row_index) + "  col_index: " + str(col_index) 
	print " distance: " 
	print distance
	''' 
	for i in range(3):
		#print distance
		direction = distance[i].split("+")[1]
		#print "direction: " + str(direction)
		if (direction == "1"):
			if recursion(memo, row_coll, col_coll, row_index - 1, col_index - 1, direc) == True:
				row_coll.append(row_index)
				col_coll.append(col_index)
				direc.append("transpose")
				return True
		elif direction == "2":
			if recursion(memo, row_coll, col_coll, row_index - 1, col_index, direc) == True:
				row_coll.append(row_index)
				col_coll.append(col_index)
				direc.append("up")
				return True
		else:
			if recursion(memo, row_coll, col_coll, row_index, col_index - 1, direc) == True:
				row_coll.append(row_index)
				col_coll.append(col_index)
				direc.append("left")
				return True


	
