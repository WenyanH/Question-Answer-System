#!/usr/bin/python
import sys, codecs, argparse
from random import shuffle
from lib import asking_easy, asking_medium, asking_hard
from lib import answering as answer
from lib.question_type import question_type
# from lib.find_possible_sentences import find_possible_sentences
from spacy.en import English

nlp = None
f_out = None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("wiki_article", help="wiki article no found")
    parser.add_argument("question_text", help="question no found")
    parser.add_argument("-o", "--output", help="output log to file")
    parser.add_argument("-v", "--verbose", help="print details log", action="store_true")
    parser.add_argument("--asking", help="run asking module", action="store_true")
    parser.add_argument("--answering", help="run answering module", action="store_true")

    args = parser.parse_args()
    if not args.wiki_article or not args.question_text:
        parser.print_help()
        sys.exit(1)

    print 'Reading data for NLP task...'
    global nlp
    nlp = English()
    print 'Done\n'

    global f_out
    if args.output:
        f_out = codecs.open(args.output, 'w', 'utf-8')
    else:
        f_out = sys.stdout

    docs = read_sentences_from_file(args.wiki_article)
    docs_q = read_sentences_from_file(args.question_text, False, True)
    if args.asking:
        asking(docs)
    if args.answering:
        answering(docs, docs_q)

def wiki_article_format(text):
    lines = [line.orth_ for line in nlp(text).sents]
    result = []
    for line in lines:
        line = line.strip()
        if len(line) < 20 or '.' not in line:
            continue
        if '\n' in line:
            line = line.split('\n')[-1]
        if 'n\'t' in line:
            line = line.replace('n\'t', ' not')
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
        if 'n\'t' in line:
            line = line.replace('n\'t', ' not')
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

def asking(docs, num_easy=5, num_medium=5, num_hard=5):
    print "Asking..."

    # sentences = [
    #     "Weixiang was born in China in 1993 .",
    #     "Guanxi is taking photos ."
    # ]
    print("\nEasy\n\n")
    count = 0
    for doc in docs:
        if count >= num_easy:
            break
        sen = get_string_of_sent(doc)
        result = asking_easy.easy_question_generator(sen)
        if result:
            f_out.write(result + '\n')
            # print sen + '\n'
            count += 1

    print("\nMedium\n\n")
    count = 0
    for doc in docs:
        if count >= num_medium:
            break
        result = asking_medium.medium_question_generator(doc, get_string_of_sent(doc))
        if result:
            f_out.write(result + '\n')
            # print doc, '\n'
            count += 1

    print("\nHard\n\n")
    count = 0
    for doc in docs:
        if count >= num_hard:
            break
        sen = get_string_of_sent(doc)
        result = asking_hard.hard_question_generator(sen)
        if result:
            f_out.write(result + '\n')
            # print sen + '\n'
            count += 1

def get_root_of_doc(doc):
    for index, token in enumerate(doc):
        if token.head is token:
            return index
    return None

def answering(docs, docs_q):
    for question_doc in docs_q:
        # print 'Answering:' + get_string_of_sent(question_doc) + '\n'
        f_out.write('Answering:' + get_string_of_sent(question_doc) + '\n\n')
        type_of_question = question_type(get_string_of_sent(question_doc), get_root_of_doc(question_doc))
        # print type_of_question

        possible_sentences_index, possible_sentences_prob = answer.find_possible_sentences(docs, question_doc)
        possible_sentences = []
        f_out.write('Possible sentences:\n')
        for index in possible_sentences_index:
            f_out.write(get_string_of_sent(docs[index]) + '\n')
            possible_sentences.append(docs[index])
        f_out.write('\n')

        f_out.write('Answer:' + '\n')
        question_answer = None
        if type_of_question == 'WH':
            question_answer = answer.answer_wh(question_doc, possible_sentences, possible_sentences_prob)
        elif type_of_question == 'YES/NO':
            question_answer = answer.answer_yesno(question_doc, possible_sentences)

        f_out.write(question_answer + '\n\n')

main()
