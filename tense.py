
# coding: utf-8

# In[22]:

from nltk.stem.wordnet import WordNetLemmatizer
import sys
sys.path.append('/Users/HWY/Desktop/MSBIC-CMU/2016Spring/11611/Project/en')  #The path of the package en. Or you can just run it on the jupyter
import en #use the nodebox english linguistics library
sys.argv   
cmdargs=list(sys.argv)
word=""
word=cmdargs[1]
#word='fantasized'
lmtzr = WordNetLemmatizer()

def originalWord(word):  #let the word becomes the original format
    return lmtzr.lemmatize(word, 'v')  #if just consider of the verb

original_word=originalWord(word)
print original_word

#print en.noun.plural("child")
#print en.noun.singular("people")
#print en.noun.is_emotion("anger")
#print en.verb.infinitive("swimming")

def tenseJudgement(word):
    return en.verb.tense(word)
tense=tenseJudgement(word)
print tense

#print en.verb.tense("was")
#print en.verb.tense("had")
#print en.verb.tense("gotten")

