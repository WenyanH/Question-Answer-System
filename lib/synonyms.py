from nltk.corpus import wordnet as wn

fout = open('synonyms.txt', 'w')
s = ''
for i in wn.all_synsets():
    if i.pos() in ['a', 's']: # If synset is adj or satelite-adj.
        for j in i.lemmas(): # Iterating through lemmas for each synset.
            if j.synset(): # If adj has antonym.
                # Prints the adj-antonym pair.
                s1 = j.synset().name().split(".")
                synonyms = s1[0]
                synonyms = synonyms.lower()
                if synonyms != j.name().lower():
                	s = j.name() + ' ' + synonyms + '\n'
                	fout.write(s)