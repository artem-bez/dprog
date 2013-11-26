"""Solution for [11/4/13] Challenge #139 [Easy] Pangrams
http://www.reddit.com/r/dailyprogrammer/comments/1pwl73/11413_challenge_139_easy_pangrams/
"""

import string
import sys
from collections import Counter
from itertools import starmap

alphabet = set(string.ascii_lowercase)


def is_pangram(iterable):
    input_chars = set(iterable)
    missing_chars = alphabet - input_chars
    return not missing_chars


def get_input():
    inputs = [None] * int(input())
    for i, __ in enumerate(inputs):
        inputs[i] = input()
    return inputs


def main():
    for i in map(str.lower, get_input()):
        print(is_pangram(i), end=' ')
        c = Counter(char for char in i if char in alphabet)
        sorted_c = sorted(c.items())
        fmted_c = starmap('{}: {}'.format, sorted_c)
        print(', '.join(fmted_c))
    return 0

if __name__ == '__main__':
    sys.exit(main())
