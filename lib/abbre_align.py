def abbre_align(align):
	align_up = []
	align_down = []

	align_up_new = []
	align_down_new = []
	abbre = []

	for item in align:
		arr = item.strip().split(",")
		align_up.append(arr[0])
		align_down.append(arr[1])

	#abbre align_up
	len_align_up = len(align_up)
	#print len_align_up
	i = 0
	while i < len_align_up:
		if (not int(align_up[i]) == -1) and (not int(align_down[i]) == -1):
			align_up_new.append(align_up[i])
			align_down_new.append(align_down[i]) 
		elif(int(align_up[i]) == -1):
			j = i + 1
			while j < len_align_up:
				#print  not (str(align_down[j]) == -1)
				if not (int(align_up[j]) == -1):
					break
				j = j + 1
			if j - i > 3:
				i =  j - 1
			else:
				for k in range(i, j):
					align_up_new.append(align_up[k])
					align_down_new.append(align_down[k])
				i = j - 1
		else:
			j = i + 1
			while j < len_align_up:
				#print  not (str(align_down[j]) == -1)
				if not (int(align_down[j]) == -1):
					break
				j = j + 1
			if j - i > 3:
				i =  j - 1
			else:
				for k in range(i, j):
					align_up_new.append(align_up[k])
					align_down_new.append(align_down[k])
				i = j - 1
		i = i + 1
	
	#print "align_up"
	#print align_up_new
	#print "align_down"
	#print align_down_new
	for i in range(len(align_down_new)):
		abbre.append(str(align_up_new[i]) + "," + str(align_down_new[i]))
	#print abbre
	return abbre

if __name__ == "__main__":
	abbre_align(["0,-1", "1,2", "2,-1", "3,-1", "4,-1", "6,2", "-1,3", "-1,4", "-1,5", "-1,6"])