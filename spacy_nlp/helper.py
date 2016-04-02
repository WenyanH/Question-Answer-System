from spacy.en import English

def build_document(text):
    # the return object is `Doc`
    # actually is an array of tokens
    # see https://spacy.io/docs#English-__call__
    nlp = English()
    doc = nlp(unicode(text))
    return doc

def doc_get_all_sents(doc):
    result = []
    for sent in doc.sents:
        result.append(sent)
    return result

def doc_get_noun_chunks(doc):
    return [chunk.orth_ for chunk in doc.noun_chunks]

def doc_get_noun_chunks_in_sent(doc, sentence):
    chunks = [chunk.orth_ for chunk in doc.noun_chunks if chunk.orth_ in sentence]
    return list(set(chunks))

def sent_get_root(sent):
    return sent.root

def token_get_base(token):
    return token.lemma_

def token_get_tag(token):
    return token.tag_

def token_get_pos(token):
    return token.pos_

if __name__ == '__main__':
    doc = build_document('Spanish is one of the six official languages of the United Nations ,  and it is used as an official language by the European Union ,  the Organization of American States ,  and the Union of South American Nations ,  among many other international organizations ?')
    print 'Doc:', doc
    print

    sent = doc_get_all_sents(doc)[0]

    for token in doc:
        print token, token_get_tag(token), token_get_pos(token), token.ent_type, token.ent_iob
    print

    print 'Root of sent:', sent_get_root(sent)
    print

    print 'parse token to its base'
    for token in doc:
        print token, '->', token_get_base(token)
    print

    print 'Noun Chunks'
    for chunk in doc.noun_chunks:
        print(chunk.label, chunk.orth_, '<--', chunk.root.head.orth_)
    print

    print 'Super sentens'
    for token in doc.ents:
        print token.orth_, token.label_
    print
