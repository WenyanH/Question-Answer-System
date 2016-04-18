#!/usr/bin/python
import sys, codecs, argparse
from random import shuffle
from lib import asking_easy, asking_medium, asking_hard, brief_sentence, question_evaluation
from lib import answering as answer
from lib.question_type import question_type
from spacy.en import English

nlp = None
wiki_title = None

def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("wiki_article", help="wiki article no found")
    # parser.add_argument("question_text", help="question no found")
    # parser.add_argument("-o", "--output", help="output log to file")
    # parser.add_argument("-v", "--verbose", help="print details log", action="store_true")
    # parser.add_argument("--asking", help="run asking module", action="store_true")
    # parser.add_argument("--answering", help="run answering module", action="store_true")
    #
    # args = parser.parse_args()
    # if not args.wiki_article or not args.question_text:
    #     parser.print_help()
    #     sys.exit(1)

    # print 'Reading data for NLP task...'
    global nlp
    nlp = English()
    # print 'Done\n'

    # docs = read_sentences_from_file(args.wiki_article)
    # docs_q = read_sentences_from_file(args.question_text, False, True)

    # if args.asking:
    #     asking(docs)
    # if args.answering:
    #     answering(docs, docs_q)

def wiki_article_format(text):
    lines = [line.orth_ for line in nlp(text).sents]
    result = []
    for line in lines:
        line = line.strip()
        if len(line) < 20 or '.' not in line:
            continue
        if '\n' in line:
            line = line.split('\n')[-1]
        if 'won\'t' in line:
            line = line.replace('won\'t', 'will not')
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
        if 'won\'t' in line:
            line = line.replace('won\'t', 'will not')
        if 'n\'t' in line:
            line = line.replace('n\'t', ' not')
        try:
            result.append(unicode(line))
        except:
            continue
    return result

def get_article_title(text):
    lines = text.split('\n')
    return unicode(lines[0].strip())

def get_article_nouns(docs):
    nouns = []
    for doc in docs:
        temp = []
        # get every words with its first letter upper case
        for index, token in enumerate(doc):
            if index == 0:
                continue
            if token.orth_[0].lower() != token.orth_[0]:
                temp.append((token.text, index))

        # merge continuous words
        past_index = -1;
        for (word, index) in temp:
            if index - 1 != past_index:
                nouns.append(word)
            else:
                nouns[len(nouns) - 1] += (unicode(' ') + word)
            past_index = index
    candidates = list(set(nouns))
    nouns = []
    for noun in candidates:
        should_be_skipped = False
        for doc in docs:
            for token in doc:
                if noun.lower() == token.orth_:
                    should_be_skipped = True
        if not should_be_skipped:
            nouns.append(noun)

    # for n in nouns:
    #     print n, ',',

    if 'I' not in nouns:
        nouns.append('I')
    return nouns

def read_sentences_from_file(file_name, wiki=True, question=False):
    text = []
    # print 'Reading file...'
    with codecs.open(file_name, encoding='utf-8') as f:
        text = f.read()
    if wiki:
        global wiki_title
        wiki_title = get_article_title(text)
        text = text.replace(wiki_title, 'wikiarticletitle')
        text = wiki_article_format(text)
    if question:
        text = question_format(text)
    # print 'Done. Parsing text...'
    docs = list(nlp.pipe(text, batch_size=50, n_threads=4))
    # print 'Done\n'
    return docs

def get_string_of_sent(sent):
    return unicode(' '.join([token.orth_ for token in sent]))

def asking(docs, num_easy=5, num_medium=5, num_hard=5):
    # print "Asking..."

    # discard some docs
    docs = list(docs)
    to_be_removed = []
    for doc in docs:
        line = get_string_of_sent(doc)
        if ';' in line or ':' in line or line.count('-') == 2 or '(' in line:
            to_be_removed.append(doc)
    for doc in to_be_removed:
        docs.remove(doc)

    # get words that should be in upper case
    upper_words = get_article_nouns(docs)

    # sentences = [
    #     "Weixiang was born in China in 1993 .",
    #     "Guanxi is taking photos ."
    # ]
    # print("\nEasy\n\n")
    # count = 0
    # print '* Easy:'
    easy_questions = []
    for doc in docs:
        # if count >= num_easy:
        #     break
        result = asking_easy.easy_question_generator(doc, get_root_of_doc(doc), upper_words)
        if result:
            try:
                result = result.replace('wikiarticletitle', wiki_title)
            except:
                continue
            result = nlp(brief_sentence.brief(nlp(result)))
            easy_questions.append(result)
            # print(result + '\n')
            # co
            # print sen + '\n'
    easy_questions = question_evaluation.question_evalution(easy_questions, docs, num_easy)
    for q in easy_questions:
        try:
            print q
        except:
            pass

    # print '*Medium'
    medium_questions = []
    for doc in docs:
        result = asking_medium.medium_question_generator(doc, get_string_of_sent(doc))
        if result:
            try:
                result = result.replace('wikiarticletitle', wiki_title)
            except:
                continue
            result = nlp(brief_sentence.brief(nlp(result)))
            medium_questions.append(result)

    medium_questions = question_evaluation.question_evalution(medium_questions, docs, num_medium)
    for q in medium_questions:
        try:
            print q
        except:
            pass

    # print '*Hard:'
    hard_questions = []
    for doc in docs:
        sen = get_string_of_sent(doc)
        result = asking_hard.hard_question_generator(sen, get_root_of_doc(doc), nlp, upper_words)
        if result:
            try:
                result = result.replace('wikiarticletitle', wiki_title)
            except:
                continue
            result = nlp(brief_sentence.brief(nlp(result)))
            hard_questions.append(result)

    hard_questions = question_evaluation.question_evalution(hard_questions, docs, num_hard)
    for q in hard_questions:
        try:
            print q
        except:
            pass

def get_root_of_doc(doc):
    for index, token in enumerate(doc):
        if token.head is token:
            return index
    return None

def get_last_token_of_doc(doc):
    result = None
    for token in doc:
        result = token
    return result

def answering(docs, docs_q):
    word_count = answer.calc_all_words_weight(docs)
    for question_doc in docs_q:
        # print('Answering:' + get_string_of_sent(question_doc) + '\n\n')
        type_of_question = question_type(get_string_of_sent(question_doc), get_root_of_doc(question_doc))
        # print type_of_question

        possible_sentences_index, possible_sentences_prob = answer.find_possible_sentences(docs, question_doc, word_count)
        possible_sentences = []
        # print('Possible sentences:\n')
        for index in possible_sentences_index:
            # try:
            #     print(get_string_of_sent(docs[index]) + '\n')
            # except:
            #     print('print fail, continue')
            #     pass
            possible_sentences.append(docs[index])
        # print('\n')

        # print('Answer:' + '\n')
        question_answer = None
        if type_of_question == 'WHAT' or type_of_question == 'WHICH':
            question_answer = answer.answer_what(question_doc, possible_sentences, possible_sentences_prob)
        elif type_of_question == 'WHERE':
            question_answer = answer.answer_where(question_doc, possible_sentences, possible_sentences_prob)
        elif type_of_question == 'WHEN':
            question_answer = answer.answer_when(question_doc, possible_sentences, possible_sentences_prob)
        elif type_of_question == 'WHY':
            question_answer = answer.answer_why(question_doc, possible_sentences, possible_sentences_prob)
        elif type_of_question == 'WHO':
            question_answer = answer.answer_who(question_doc, possible_sentences, possible_sentences_prob)
        elif type_of_question == 'YES/NO':
            question_answer = answer.answer_yesno(question_doc, possible_sentences)
        else:
            # HOW *
            word = get_last_token_of_doc(nlp(unicode(type_of_question)))
            if word.pos_ == 'VERB':
                question_answer = answer.answer_how(question_doc, possible_sentences, possible_sentences_prob)
            else:
                question_answer = answer.answer_how_something(question_doc, possible_sentences, possible_sentences_prob, type_of_question)

        # Upper the first letter of question_answer
        question_answer = question_answer[0].upper() + question_answer[1:]
        try:
            question_answer = question_answer.replace('wikiarticletitle', wiki_title)
            print(question_answer)
        except:
            # print('answer print fail, continue')
            print("")
            pass


if __name__ == '__main__':
    main()
