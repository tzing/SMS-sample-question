#!/usr/bin/env python
"""Check if there exists the duplicated question in the true and false question.
"""
import argparse
import re

INDENT_SPACE = 4
TAB_SPACE = 6


def main():
    # parse question
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'file', type=argparse.FileType(), help='file to be checked')
    parser.add_argument(
        '-v', '--verbose', action='store_true', help='enable verbose mode')

    args = parser.parse_args()

    # read table
    qa_pattern = re.compile(
        r'\|\s*(?P<ans>\w)\s*\|\s*(?P<question>.+)\s*\|?\s*')

    questions = []
    for n_line, string in enumerate(args.file, 1):  # line number starts at 1
        # search for table
        match = qa_pattern.match(string)
        if not match:
            if args.verbose:
                print('not match: ' + string.strip())
            continue

        # retrieve question and answer
        ans = match.group('ans').upper()

        question = match.group('question')
        question = re.sub('\s', '', question)
        question = question.replace(',', '，')
        question = question.replace(':', '：')
        question = question.replace(';', '；')
        question = question.replace('(', '（')
        question = question.replace(')', '）')
        question = question.replace('?', '？')

        questions.append((n_line, ans, question))

    # compare
    unique_question = {}
    duplicate_questions = {}

    for n, a, q in questions:
        if q in unique_question:
            current_ans = duplicate_questions.get(q, unique_question[q])
            current_ans.append((n, a))
            duplicate_questions[q] = current_ans
        else:
            unique_question[q] = [(n, a)]

    # show result
    if len(duplicate_questions) == 0:
        print('Everything is fine :)')
        exit(0)

    else:
        print('Duplicated questions:')
        indent = ' ' * INDENT_SPACE
        for q, dups in duplicate_questions.items():
            print(indent + q)
            print(indent * 2 + 'line\tans'.expandtabs(TAB_SPACE))
            for n, a in dups:
                msg = '{n}\t{a}'.format(n=n, a=a)
                msg = msg.expandtabs(TAB_SPACE)
                print(indent * 2 + msg)
        exit(1)


if __name__ == '__main__':
    main()
