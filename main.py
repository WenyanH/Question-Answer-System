import sys
from lib import asking_easy, asking_medium

def main():
    asking()

def asking(num_easy=2, num_medium=1, num_hard=1):
    print "Asking..."

    # prepare text
    # TODO: pick_sentences_from_file() @wenyanhu


    sentences = [
        "Weixiang was born in China in 1993 .",
        "Guanxi is taking photos ."
    ]

    print "\tEasy"
    for i in range(num_easy):
        if i >= len(sentences): break
        result = asking_easy.easy_question_generator(sentences[i])
        if result:
            print "\t\t" + result

    print "\tMedium"
    for i in range(num_medium):
        if i >= len(sentences): break
        result = asking_medium.medium_question_generator(sentences[i])
        if result:
            print "\t\t" + result

    print "\tHard"
    for i in range(num_hard):
        if i >= len(sentences): break
        # TODO: finish asking_hard module

main()
