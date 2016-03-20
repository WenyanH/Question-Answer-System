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

def sent_get_root(sent):
    return sent.root

def token_get_base(token):
    return token.lemma_

def token_get_tag(token):
    return token.tag_

def token_get_pos(token):
    return token.pos_

if __name__ == '__main__':
    doc = build_document('Students who were taught by Allen Black win the awards.')
    print 'Doc:', doc
    print

    sent = doc_get_all_sents(doc)[0]
    print 'Tokens:'
    for token in sent:
        print token, token_get_tag(token), token_get_pos(token)
    print

    print 'Noun Chunks'
    for chunk in doc.noun_chunks:
        print(chunk.label, chunk.orth_, '<--', chunk.root.head.orth_)
    print

    print 'Root of sent:', sent_get_root(sent)
    print

    print 'parse token to its base'
    tokens = build_document('goes went read written had being cried running men')
    for token in tokens:
        print token, '->', token_get_base(token)
