import nltk

def main():
    test = [
        "I am eating now",
        "He went to Pittsburgh",
        "Marry has visited here $time$",
        "I went to $place$ last night"
    ]
    for t in test:
        print t, '->', convert_declarative_to_question(t)

def is_sentence_perfect(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    tagged = [x[1] for x in tagged]
    # print tagged, sentence

    # # the first tag should be NN*
    # if tagged[0][:2] != 'NN':
    #     return False

    # VB* should exist in tags
    for tag in tagged:
        if tag[:2] == 'VB':
            break
    else:
        return False

    return True

def convert_declarative_to_question(sentence):
    if sentence is None:
        return None
    if not is_sentence_perfect(sentence):
        return None
    words = sentence.split(' ')
    if words[0] != 'I':
        words[0] = words[0][0].lower() + words[0][1:]
    words = _convert_declarative_to_question_without_wh(words)
    if '$time$' in words:
        words.insert(0, 'When')
        words.remove('$time$')
    elif '$place$' in words:
        words.insert(0, 'Where')
        words.remove('$place$')

    words[0] = words[0][0].upper() + words[0][1:]
    return ' '.join(words)

def _convert_declarative_to_question_without_wh(words):
    target = ['have', 'has', 'had', 'is', 'are', 'am', 'were', 'was', 'will']
    for key in target:
        if key in words:
            words.remove(key)
            words.insert(0, key)
            break
    else:
        words.insert(0, 'does')
    return words

if __name__ == '__main__':
    main()
