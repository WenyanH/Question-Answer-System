import os, sys

'''
Usage: python split.py xxx1/ xxx2/
'''

for directory in sys.argv[1:]:
    for file_name in os.listdir(directory):
        path = directory + file_name
        if '_raw' in path or '_answer' in path or '_question' in path or '.txt' not in path:
            continue
        print 'Splitting', path, '...'
        output_question = ''
        output_answer = ''
        with open(path) as f:
            for line in f:
                line = line.strip().split('\t')
                if len(line) != 2:
                    print 'Meet Error when splitting this line:', line
                    continue
                output_question = output_question + line[0] + '\n'
                output_answer = output_answer + line[1] + '\n'
        path_question = path.replace('.txt', '_question.txt')
        with open(path_question, 'w') as f:
            f.write(output_question)
        path_answer = path.replace('.txt', '_answer.txt')
        with open(path_answer, 'w') as f:
            f.write(output_answer)
