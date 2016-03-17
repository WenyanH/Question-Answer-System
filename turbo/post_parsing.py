import turbo_describe
import sys

def main():
    conll_sentences = []
    sentence = []
    for line in sys.stdin:
        if line.strip() != '':
            sentence.append(line)
        elif len(sentence) != 0:
            # print sentence
            conll_sentences.append(turbo_describe.read_data(sentence))
            sentence = []

    for line in conll_sentences:
        print line


if __name__ == '__main__':
    main()
