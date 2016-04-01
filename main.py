import sys
from random import shuffle
from lib import asking_easy, asking_medium, asking_hard, helper
from lib import answering as answer
from lib.question_type import question_type
# from lib.find_possible_sentences import find_possible_sentences
from spacy_nlp import helper as spacy_helper

def main():
    if len(sys.argv) != 3:
        print 'usage: python main.py input.txt question.txt'
        sys.exit(1)

    doc, sentences = read_sentences_from_file(sys.argv[1])
    doc_q, questions = read_sentences_from_file(sys.argv[2], False, True)
    # asking(sentences, doc)
    answering(doc, sentences, doc_q, questions)

def wiki_article_format(text):
    # TODO:
    # remove some unrelated sentences like external links
    lines = text.split('\n')
    result = []
    for line in lines:
        line = line.strip()
        if len(line) < 20 or '.' not in line:
            continue
        try:
            result.append(unicode(line))
        except:
            continue
    return ' '.join(result)

def question_format(text):
    lines = text.split('\n')
    result = []
    for line in lines:
        line = line.strip()
        if len(line) < 20 or '?' not in line:
            continue
        try:
            result.append(unicode(line))
        except:
            continue
    return ' '.join(result)

def read_sentences_from_file(file_name, wiki=True, question=False):
    text = None
    print 'Reading file...'
    with open(file_name) as f:
        text = f.read()
    if wiki:
        text = wiki_article_format(text)
    if question:
        text = question_format(text)
    print 'Done. Parsing text...'
    doc = spacy_helper.build_document(text)
    sents = spacy_helper.doc_get_all_sents(doc)
    print 'Done'
    print
    return doc, sents

def get_string_of_sent(sent):
    return ' '.join([token.orth_ for token in sent])

def get_string_of_text(sent_array):
    text = []
    for sent in sent_array:
        text.append([token.orth_ for token in sent])
    return text


def asking(sentences, doc, num_easy=5, num_medium=5, num_hard=5):
    print "Asking...\n"

    # sentences = [
    #     "Weixiang was born in China in 1993 .",
    #     "Guanxi is taking photos ."
    # ]
    print "Easy\n"
    count = 0
    for sen in sentences:
        if count >= num_easy:
            break
        sen = get_string_of_sent(sen)
        result = asking_easy.easy_question_generator(sen)
        if result:
            print result
            # print sen + '\n'
            print '\n'
            count += 1

    print "Medium\n"
    count = 0
    for sen in sentences:
        if count >= num_medium:
            break
        sen = get_string_of_sent(sen)
        result = asking_medium.medium_question_generator(sen, doc.noun_chunks)
        if result:
            print result
            print sen + '\n'
            count += 1

    print "Hard\n"
    count = 0
    for sen in sentences:
        if count >= num_hard:
            break
        sen = get_string_of_sent(sen)
        result = asking_hard.hard_question_generator(sen)
        if result:
            print result
            print sen + '\n'
            count += 1

def answering(doc, sentences, doc_q, questions):
    text_2d_array = get_string_of_text(sentences)

    for sent in questions:
        question_token = get_string_of_sent(sent)
        question_tags = [token.pos_ for token in sent]

        possible_sentences_index = answer.find_possible_sentences(doc, sent)
        # print 'Question:', sent
        # for index, token in enumerate(sent):
        #     if token.head is token:
        #         print 'Root:', index, token
        #         print 'Type:', question_type(get_string_of_sent(sent), index)
        # print sent
        # print spacy_helper.doc_get_all_sents(doc)[possible_sentences_index[0]]

        possible_sentences = []
        noun_chunks_list = []

        for index in possible_sentences_index:
            possible_sentences.append(spacy_helper.doc_get_all_sents(doc)[index])
            poss_sentence_token = ' '.join(text_2d_array[index])
            noun_chunks_list.append(spacy_helper.doc_get_noun_chunks_in_sent(doc, poss_sentence_token))

        # answer.answer_yesno(sent, possible_sentences)
        answer.answer_what(sent, possible_sentences, noun_chunks_list)
        break

        # print ' '.join(text_2d_array[possible_sentences_index[0]])

main()
