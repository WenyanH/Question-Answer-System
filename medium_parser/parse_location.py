import re

def parse_time(text):
	f = open('location.txt', 'r')
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

print(parse_time('ds dsa dw Guangzhou shsh rfq'))	
print(parse_time('tiantui loves Shanghai girls'))	