import string
def question_type(line, position):
	#can not judge negation sentences
	#line unicode
	#print type(line)
	#print "position:" + str(position)
	#collection
	col = ["is", "are", "am", "was", "were"]
	col_up = ["Is", "Are", "Am", "Was", "Were"]
	#question words
	question_word = ["what", "What", "How", "how", "when", "When", "Where", "where", "who", "Who", "Why", "why"]


	line = line.strip()
	#strategy 1: find question words.
	#if question words are not in the sentence, return "YES/NO"
	arr = line.split(" ")
	
	#if position == 0, root can not be question words.
	if position == 0:
		if arr[0] in question_word: 
			return "WH"
		return "YES/NO"
		#type(arr[0])
	index = 0
	for i in range(len(question_word)):
		if question_word[i] in arr:
			break;
		else:
			index = index + 1;
	if index == len(question_word):
		return "YES/NO"

	#strategy 2: Use dependency tree to find the root in the sentence.
	#if the root is "BE", find question words; if the root is verb, find "BE";
	mark = -1
	#iterate each word to find the boundary
	for j in range(position):
		#determine whether number or alphabet
		sign = False
		for i in range(len(arr[j])):
			if arr[j].strip()[i] in string.ascii_letters or arr[j].strip()[i] in string.digits:
				sign = True
				break
			#record the location of none-alnum
		if sign == False:
			mark = j
			# print "mark       " + str(mark)		
	#print "mark" + str(mark)
	#if arr[position] in col or arr[position] in col_up:
		#find question words
	for k in range(mark + 1, position):
		if arr[k] in question_word:
			return "WH"
	return "YES/NO"
	'''
	else:
		#find "BE"
		for k in range(mark + 1, position):
			if arr[k] in col or arr[k] in col_up:
				return "YES/NO"
		return "WH"
	'''	
if __name__ == "__main__":
	'''
	print question_type("nning in the early 16th century ,  was Spanish taken to the colonies of the Spanish Empire ,  most notably to the Americas ,  as well as territories in Africa ,  Oceania and the Philippines ?", 10)
	print question_type("What is one of the six official languages of the United Nations ,  and it is used as an official language by the European Union ,  the Organization of American States ,  and the Union of South American Nations ,  among many other international organizations ?", 1)
	print question_type("Who claims that there are an estimated 470 million Spanish speakers with native competence and 559 million Spanish speakers as a first or second language ,  including speakers with limited competence and more than 21 million students of Spanish as a foreign language ?", 1)
	print question_type("When was it estimated by the American Community Survey that of the 55 million Hispanic United States residents who are five years of age and over ,  38 million speak Spanish at home ?", 30)
	print question_type("When was Spanish an official language of the Philippines from the beginning of Spanish rule in 1565 to a constitutional change ?", 1)
	'''
	print question_type("When he is at home , is he playing ?", 8)
	print question_type("When he is at home , what is his name ?", 7)
	#print question_type("Is he playing when he is at home ?", 2)
	print question_type("It is a good day , what time is it ?", 8)
	'''
	print question_type("What time is it , it is a good day ?", 2)
	print question_type("Due to precession ,  what will move closer to the South Pole in the next millennia ,  up to 67 degrees south declination for the middle of the constellation ?", 7)
	print question_type("Due to precession ,  will Crux move closer to the South Pole in the next millennia ,  up to 67 degrees south declination for the middle of the constellation ?",6)
	print question_type("But in AD 18000 or BC 8000 will Crux be less than 30 degrees south declination making it visible in Northern Europe ?", 9)
	print question_type("But in AD 18000 or BC 8000, will Crux be less than 30 degrees south declination making it visible in Northern Europe ?", 10)
	print question_type("Will but in AD 18000 or BC 8000 Crux be less than 30 degrees south declination making it visible in Northern Europe ?", 0)
	'''
