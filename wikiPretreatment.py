
# coding: utf-8

# In[140]:

import re
import sys
sys.argv   
cmdargs=list(sys.argv)

#inputfile=open('raw4.txt', 'r')
#outputfile=open('data.txt','wb')
inputfile=open(cmdargs[1], 'r')
outputfile=open(cmdargs[2],'wb')
words=""
for word in inputfile.read(): 
    words=words+word
words=words.replace('.',' . ').replace('?',' ? ').replace('!',' ! ').replace('\n\n', '\n')
words=words.split(" ")
for i in range(0, len(words)):
    words[i]=words[i].replace(',',' , ').replace(':',' : ').replace('(',' ( ').replace(')',' ) ').replace('/',' / ').replace('\"',' \" ').replace('\'',' \' ')

#Decide whether start a newline or not according to the next word's first character or the '\n'
text=""
for i in range(0, len(words)): 
    if words[i]!='':
        if words[i]=='.' or words[i]=='?' or words[i]=='!': 
            if i==len(words)-2:
                text=text+words[i]
            elif words[i+1][:1]=='\n':
                text=text+words[i]
            elif words[i+1][1:2].isupper():
                    text=text+words[i]+'\n'
            elif words[i+2][:1].isupper():
                if i<len(words)-3 and words[i+3]!='.':
                    text=text+words[i]+'\n'      
                else: 
                    text=text+words[i]+' '
            else:
                text=text+words[i]+' '
        else:
            text=text+words[i]+' '
outputfile.write(text)
outputfile.close()   #now every line ends up with a space, you can use xxx.strip() to remove it when you use the file

