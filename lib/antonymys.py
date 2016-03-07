from nltk.corpus import wordnet as wn

fout = open('antonyms.txt', 'w')
s = ''
for i in wn.all_synsets():
    if i.pos() in ['a', 's']: # If synset is adj or satelite-adj.
        for j in i.lemmas(): # Iterating through lemmas for each synset.
            if j.antonyms(): # If adj has antonym.
                # Prints the adj-antonym pair.
                s = j.name() + ' ' + j.antonyms()[0].name() + '\n'
                fout.write(s)