#!/usr/bin/env python3
"""Check if there exists the duplicated question in the true and false question.
"""
import argparse
import re
import unicodedata

INDENT_SPACE = 4
TAB_SPACE = 6

CHINESE_DIGITS = "零一二三四五六七八九"
CHINESE_UNITS = "十百千"


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

        # unified symbols
        question = match.group('question')
        question = re.sub('\s', '', question)
        question = unicodedata.normalize('NFKC', question)

        # unified number
        for m in reversed(list(re.finditer(r'\d+', question))):
            number = integer2chinese(int(m.group()))
            question = question[:m.start()] + number + question[m.end():]

        # unified text
        question = question.replace('替代役役男', '替代役男')
        question = question.replace('半年', '六個月')
        question = question.replace('兩', '二')
        question = re.sub(r'。$', '', question)

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


def integer2chinese(num):
    """Convert integers into chinese representation.
    """
    assert isinstance(num, int)

    # number to chinese
    num_name = ""
    level = 0
    while num > 0:
        num_name = get_chinese_number_name(level, num % 10) + num_name
        num = num // 10
        level += 1

    # remove zeros
    num_name = re.sub(r'零+$', '', num_name)  # tailing zeros
    num_name = re.sub(r'零+', '零', num_name)  # continue zeros

    return num_name


def get_chinese_number_name(level, number):
    # number name
    if number == 0:
        return CHINESE_DIGITS[0]
    name = CHINESE_DIGITS[number]

    # level unit
    if level == 1 and number == 1:
        return CHINESE_UNITS[0]
    elif level > 0:
        name += CHINESE_UNITS[level % 4 - 1]

    return name


if __name__ == '__main__':
    main()
