import re
from lib import helper

def medium_question_generator(line):
	line = parse_time(line) or parse_location(line)
	return helper.convert_declarative_to_question(line)

def parse_location(text):
	f = open('data/location.txt', 'r')
	cities = []
	for line in f:
		cities.append(line.rstrip())
	text = text.strip()
	words = re.split(" ", text)
	count = 0
	for i in range(len(words)):
		if words[i] in cities:
			count += 1
			words[i] = '$place$'
	if count == 1:
		s = ''
		for word in words:
			s += word + ' '
		return s.strip()
	else:
		return None

def parse_time(text):
	Months = {'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'}
	Weeks = {'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'}
	time = {'am', 'pm', 'AM', 'PM', 'a.m.', 'p.m.', 'A.M.', 'P.M.'}
	text = text.strip()
	s = ''
	words = re.split(" ", text)
	for i in range(len(words)):
		if words[i] in Months or words[i] in Weeks:
			words[i] = '$time$'
		elif words[i] in time:
			if i-1 >= 0:
				words[i-1] = '$time$'
			words[i] = '$time$'
		elif len(words[i]) == 4:
			if words[i].isdigit():
				if int(words[i])>=1800 and int(words[i])<= 2100:
					words[i] = '$time$'
		else:
			continue
	flag = True
	for word in words:
		if word == '$time$':
			if flag == True:
				s += word + ' '
				flag = False
		else:
			s += word + ' '
	return s.strip()

if __name__ == "__main__":
	print(parse_time("Weixiang was born in China in 1993 ."))
	print(parse_location('ds dsa dw Guangzhou shsh rfq'))
	print(parse_location('tiantui loves Shanghai girls'))
