import sys, re

if len(sys.argv) != 2:
    print 'usage: python pre_parsing.py <input>'
    sys.exit(1)

lines = []
with open(sys.argv[1]) as f:
    lines = f.readlines()

with open(sys.argv[1], 'w') as f:
    for line in lines:
        line = re.sub('\(.*\)', '', line)
        line = re.sub(',', '', line)
        line = re.sub('-.*-', '', line)
        
        f.write(line + '\n')
