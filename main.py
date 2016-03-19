import sys
from random import shuffle
from lib import asking_easy, asking_medium, asking_hard, helper
from spacy_nlp import helper as spacy_helper

def main():
    if len(sys.argv) != 2:
        print 'usage: python main.py input.txt'
        sys.exit(1)

    doc, sentences = read_sentences_from_file(sys.argv[1])
    asking(sentences)

def wiki_article_format(text):
    # TODO:
    # remove some unrelated sentences like external links
    lines = text.split('\n')
    result = []
    for line in lines:
        if len(line) < 10:
            continue
        try:
            result.append(unicode(line))
        except:
            continue
    return ' '.join(result)

def read_sentences_from_file(file_name):
    text = None
    print 'Reading file...'
    with open(file_name) as f:
        text = f.read()
    text = wiki_article_format(text)
    print 'Done. Parsing text...'
    doc = spacy_helper.build_document(text)
    sents = spacy_helper.doc_get_all_sents(doc)
    print 'Done'
    print
    return doc, sents

def get_string_of_sent(sent):
    return ' '.join([token.orth_ for token in sent])

def asking(sentences, num_easy=5, num_medium=5, num_hard=5):
    print "Asking..."

    # sentences = [
    #     "Weixiang was born in China in 1993 .",
    #     "Guanxi is taking photos ."
    # ]
    print "\tEasy"
    count = 0
    for sen in sentences:
        if count >= num_easy:
            break
        sen = get_string_of_sent(sen)
        result = asking_easy.easy_question_generator(sen)
        if result:
            print "\t\t" + result
            print "\t\t-" + sen
            count += 1

    # print "\tMedium"
    # count = 0
    # for sen in sentences:
    #     if count >= num_medium:
    #         break
    #     result = asking_medium.medium_question_generator(sen)
    #     if result:
    #         print "\t\t" + result
    #         print "\t\t-" + sen
    #         count += 1

    print "\tHard"
    count = 0
    for sen in sentences:
        if count >= num_hard:
            break
        sen = get_string_of_sent(sen)
        result = asking_hard.hard_question_generator(sen)
        if result:
            print "\t\t" + result
            print "\t\t-" + sen
            count += 1

main()
