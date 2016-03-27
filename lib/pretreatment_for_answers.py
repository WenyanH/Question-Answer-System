
# coding: utf-8

# In[17]:

#Now all for the "BE" sentences
import nltk
be=['is', 'am','are','was','were']

def pretreatment(s):
    tokens = nltk.word_tokenize(s.lower())
    sentence=list()
    for i in range(0, len(tokens) - 1):
        if tokens[i]=="n't":
            tokens[i]="not"
        if tokens[i] not in be:
            sentence.append(tokens[i])
    return sentence

def output(s1, s2):
    return pretreatment(s1), pretreatment(s2)
    
if __name__ == "__main__":
    s1="Is she a teacher?"
    s2="She isn't a student."
    print output(s1, s2)

