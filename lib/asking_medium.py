import re
import helper

def medium_question_generator(line):
	line = parse_time(line) or parse_location(line)
	return helper.convert_declarative_to_question(line)

def parse_location(text):
	prep = {'at', 'on', 'in', 'before', 'after', 'by', 'around'}
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
		for i in range(len(words)):
			if words[i] in prep and words[i+1] == '$place$':
				continue
			s += words[i] + ' '
		return s.strip()
	else:
		return None

def parse_time(text):
	Months = {'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'}
	Weeks = {'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'}
	time = {'am', 'pm', 'AM', 'PM', 'a.m.', 'p.m.', 'A.M.', 'P.M.'}
	prep = {'at', 'on', 'in', 'before', 'after', 'by', 'around'}
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
	for i in range(len(words)):
		if words[i] == '$time$':
			if flag == True:
				s += words[i] + ' '
				flag = False
		else:
			if words[i] in prep and words[i+1] == '$time$':
				continue
			s += words[i] + ' '
	if '$time$' in s.strip():
		return s.strip()
	else:
		return None

if __name__ == "__main__":
	print(parse_time("Weixiang was born in China in 1993 ."))
	print(parse_location('XiChen is always taking photoes at Shanghai .'))
	print(parse_location('Tiantui loves dating with girls at Shanghai .'))
	#print(parse_location('Tiantui loves dating with girls at Shanghai .'))
