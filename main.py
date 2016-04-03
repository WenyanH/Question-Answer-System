import sys, codecs
from random import shuffle
from lib import asking_easy, asking_medium, asking_hard
from lib import answering as answer
from lib.question_type import question_type
# from lib.find_possible_sentences import find_possible_sentences
from spacy.en import English

nlp = None
f_out = None

def main():
    if len(sys.argv) != 4:
        print 'usage: python main.py input.txt question.txt output'
        sys.exit(1)

    print 'Reading data for NLP task...'
    global nlp
    nlp = English()
    print 'Done\n'

    global f_out
    f_out = codecs.open(sys.argv[3], 'w', 'utf-8')

    docs = read_sentences_from_file(sys.argv[1])
    docs_q = read_sentences_from_file(sys.argv[2], False, True)
    # asking(docs)
    answering(docs, docs_q)

def wiki_article_format(text):
    # TODO:
    # remove some unrelated sentences like external links
    lines = [line.orth_ for line in nlp(text).sents]
    result = []
    for line in lines:
        line = line.strip()
        if len(line) < 20 or '.' not in line:
            continue
        try:
            result.append(unicode(line))
        except:
            continue
    return result

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
    return result

def read_sentences_from_file(file_name, wiki=True, question=False):
    text = []
    print 'Reading file...'
    with codecs.open(file_name, encoding='utf-8') as f:
        text = f.read()
    if wiki:
        text = wiki_article_format(text)
    if question:
        text = question_format(text)
    print 'Done. Parsing text...'
    docs = list(nlp.pipe(text, batch_size=50, n_threads=4))
    print 'Done\n'
    return docs

def get_string_of_sent(sent):
    return unicode(' '.join([token.orth_ for token in sent]))
#
# def get_string_of_text(sent_array):
#     text = []
#     for sent in sent_array:
#         text.append([token.orth_ for token in sent])
#     return text


def asking(docs, num_easy=5, num_medium=5, num_hard=5):
    print "Asking...\n"

    # sentences = [
    #     "Weixiang was born in China in 1993 .",
    #     "Guanxi is taking photos ."
    # ]
    f_out.write("Easy\n")
    count = 0
    for doc in docs:
        if count >= num_easy:
            break
        sen = get_string_of_sent(doc)
        result = asking_easy.easy_question_generator(sen)
        if result:
            f_out.write(result)
            # print sen + '\n'
            count += 1

    f_out.write("Medium\n")
    count = 0
    for doc in docs:
        if count >= num_medium:
            break
        result = asking_medium.medium_question_generator(doc, get_string_of_sent(doc))
        if result:
            f_out.write(result)
            # print doc, '\n'
            count += 1

    f_out.write("Hard\n")
    count = 0
    for doc in docs:
        if count >= num_hard:
            break
        sen = get_string_of_sent(doc)
        result = asking_hard.hard_question_generator(sen)
        if result:
            f_out.write(result)
            # print sen + '\n'
            count += 1

def get_root_of_doc(doc):
    for index, token in enumerate(doc):
        if token.head is token:
            return index
    return None

def answering(docs, docs_q):
    # text_2d_array = get_string_of_text(sentences)
    for question_doc in docs_q:
        print 'Answering:' + get_string_of_sent(question_doc) + '\n'
        f_out.write('Answering:' + get_string_of_sent(question_doc) + '\n\n')
        type_of_question = question_type(get_string_of_sent(question_doc), get_root_of_doc(question_doc))
        # print type_of_question
        possible_sentences_index, possible_sentences_prob = answer.find_possible_sentences(docs, question_doc)
        # print 'Question:', sent
        # for index, token in enumerate(sent):
        #     if token.head is token:
        #         print 'Root:', index, token
        #         print 'Type:', question_type(get_string_of_sent(sent), index)
        # print sent
        # print spacy_helper.doc_get_all_sents(doc)[possible_sentences_index[0]]

        possible_sentences = []
        f_out.write('Possible sentences:\n')
        for index in possible_sentences_index:
            f_out.write(get_string_of_sent(docs[index]) + '\n')
            possible_sentences.append(docs[index])
        f_out.write('\n')

        # question_answer = answer.answer_yesno(question_doc, possible_sentences)
        # print question_answer
        # break
        f_out.write('Answer:' + '\n')
        question_answer = None
        if type_of_question == 'WH':
            question_answer = answer.answer_what(question_doc, possible_sentences, possible_sentences_prob)
            question_answer = get_string_of_sent(question_answer)
        elif type_of_question == 'YES/NO':
            question_answer = answer.answer_yesno(question_doc, possible_sentences)

        f_out.write(question_answer + '\n\n')

main()
