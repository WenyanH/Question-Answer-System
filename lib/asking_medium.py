import re

def medium_question_generator(doc, sentence):
	return asking_wh(doc, sentence)

def create_question(sentence, replace_from, replace_to):
	if replace_from.lower() in ['it', 'that', 'this', 'these', 'those', 'he', 'she', 'they', 'his', 'him', 'her', 'their', 'its']:
		return None
	sentence = sentence.replace(replace_from, replace_to, 1)
	sentence = sentence[:-1] + '?'
	return sentence

def asking_wh(doc, sentence):
	# Who / When / Where Question
	ent = list(doc.ents)[0] if len(doc.ents) > 0 else None
	if ent and sentence.startswith(ent.orth_) and get_next_token_pos(doc, ent) == 'VERB':
		if ent.label_ in ['PERSON']:
			question = create_question(sentence, ent.orth_, 'Who')
			question = question.replace('Who \'s', 'Whose')
			return question
		elif ent.label_ in ['LOC', 'LOC']:
			return create_question(sentence, ent.orth_, 'Where')
		# elif ent.label_ in ['DATE', 'TIME']:
		# 	return create_question(sentence, ent.orth_, 'When')
		elif ent.label_ in ['ORG', 'NORP', 'PRODUCT', 'EVENT', 'WORK_OF_ART', 'LAW', 'LANGUAGE']:
			return create_question(sentence, ent.orth_, 'What')
		elif ent.label_ in ['CARDINAL']:
			return create_question(sentence, ent.orth_, 'How many')

	# What Question
	# try:
	# 	chunk = doc.noun_chunks.next()
	# 	if chunk and sentence.startswith(chunk.orth_):
	# 		if sentence.startswith(chunk.orth_):
	# 			return create_question(sentence, chunk.orth_, 'What')
	# except:
	# 	pass
	return None

def get_next_token_pos(doc, ent):
	for token in doc:
		if token.orth_ not in ent.orth_:
			return token.pos_
	return None
#
# def parse_location(text):
# 	prep = {'at', 'on', 'in', 'before', 'after', 'by', 'around'}
# 	f = open('data/location.txt', 'r')
# 	cities = []
# 	for line in f:
# 		cities.append(line.rstrip())
# 	text = text.strip()
# 	words = re.split(" ", text)
# 	count = 0
# 	for i in range(len(words)):
# 		if words[i] in cities:
# 			count += 1
# 			words[i] = '$place$'
# 	if count == 1:
# 		s = ''
# 		for i in range(len(words)):
# 			if words[i] in prep and words[i+1] == '$place$':
# 				continue
# 			s += words[i] + ' '
# 		return s.strip()
# 	else:
# 		return None
#
# def parse_time(text):
# 	Months = {'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'}
# 	Weeks = {'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'}
# 	time = {'am', 'pm', 'AM', 'PM', 'a.m.', 'p.m.', 'A.M.', 'P.M.'}
# 	prep = {'at', 'on', 'in', 'before', 'after', 'by', 'around'}
# 	text = text.strip()
# 	s = ''
# 	words = re.split(" ", text)
# 	for i in range(len(words)):
# 		if words[i] in Months or words[i] in Weeks:
# 			words[i] = '$time$'
# 		elif words[i] in time:
# 			if i-1 >= 0:
# 				words[i-1] = '$time$'
# 			words[i] = '$time$'
# 		elif len(words[i]) == 4:
# 			if words[i].isdigit():
# 				if int(words[i])>=1800 and int(words[i])<= 2100:
# 					words[i] = '$time$'
# 		else:
# 			continue
# 	flag = True
# 	for i in range(len(words)):
# 		if words[i] == '$time$':
# 			if flag == True:
# 				s += words[i] + ' '
# 				flag = False
# 		else:
# 			if words[i] in prep and words[i+1] == '$time$':
# 				continue
# 			s += words[i] + ' '
# 	if '$time$' in s.strip():
# 		return s.strip()
# 	else:
# 		return None

if __name__ == "__main__":
	print(parse_time("Weixiang was born in China in 1993 ."))
	print(parse_location('XiChen is always taking photoes at Shanghai .'))
	print(parse_location('Tiantui loves dating with girls at Shanghai .'))
	#print(parse_location('Tiantui loves dating with girls at Shanghai .'))
