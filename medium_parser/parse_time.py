import re

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



print(parse_time("dsadas dsa sa Monday March 2:00 pm 31231 1892 4124 411"))