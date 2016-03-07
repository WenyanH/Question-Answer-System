import sys
from random import shuffle
from lib import asking_easy, asking_medium

def main():
    if len(sys.argv) != 2:
        print 'usage: python main.py input.txt'
        sys.exit(1)

    sentences = read_sentences_from_file(sys.argv[1])
    asking(sentences)

def read_sentences_from_file(file_name):
    sentences = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            # Remove the things between '(' and ')'
            while '(' in line and ')' in line:
                start, end = line.find('('), line.find(')')
                line = line[:start].strip() + ' ' + line[end+1:].strip()

            if '-' in line:
                start, end = line.find('-'), line.rfind('-')
                line = line[:start].strip() + ' ' + line[end+1:].strip()

            # Drop the line according to some rules
            if ':' in line or '/' in line or len(line) < 3 or len(line.split(' ')) < 3:
                continue

            # Drop the sentences with one comma
            # Or Remove the comma part if there exists two comma
            if len(line.split(',')) == 3:
                start, end = line.find(','), line.rfind(',')
                line = line[:start].strip() + ' ' + line[end+1:].strip()
            else:
                continue

            sentences.append(line)
    shuffle(sentences)
    # sentences.sort(key = lambda s: len(s))

    return sentences

def asking(sentences, num_easy=5, num_medium=5, num_hard=1):
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
        result = asking_easy.easy_question_generator(sen)
        if result:
            print "\t\t" + result
            print "\t\t-" + sen
            count += 1

    print "\tMedium"
    count = 0
    for sen in sentences:
        if count >= num_medium:
            break
        result = asking_medium.medium_question_generator(sen)
        if result:
            print "\t\t" + result
            print "\t\t-" + sen
            count += 1

    print "\tHard"
    count = 0
    for sen in sentences:
        if count >= num_hard:
            break
        # TODO: finish asking_hard module

main()
