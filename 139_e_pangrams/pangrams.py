"""Solution for [11/4/13] Challenge #139 [Easy] Pangrams
http://www.reddit.com/r/dailyprogrammer/comments/1pwl73/11413_challenge_139_easy_pangrams/
"""

import string
import sys
from collections import Counter
from itertools import starmap

ALPHABET = set(string.ascii_lowercase)


def is_pangram(iterable):
    input_chars = set(iterable)
    missing_chars = ALPHABET - input_chars
    return not missing_chars


def get_input():
    inputs = [None] * int(input())
    for i, __ in enumerate(inputs):
        inputs[i] = input()
    return inputs


def print_letters(letters):
    sorted_letters = sorted(letters.items())
    fmted_letters = starmap('{}: {}'.format, sorted_letters)
    print(', '.join(fmted_letters))


def main():
    for i in map(str.lower, get_input()):
        letters = Counter(char for char in i if char in ALPHABET)
        print(is_pangram(letters), end=' ')
        print_letters(letters)
    return 0

if __name__ == '__main__':
    sys.exit(main())
