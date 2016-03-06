def main():
    test = [
        "I am eating now",
        "He went to Pittsburgh",
        "Marry has visited here $time$",
        "I went to $place$ last night"
    ]
    for t in test:
        print t, '->', convert_declarative_to_question(t)

def convert_declarative_to_question(sentence):
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
    else:
        return None

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
