#!/usr/bin/env python

"""A simple python script for Rosalind a problem.
"""

__author__ = "Wytamma Wirth"
__license__ = "MIT"
__version__ = "2.2"

import argparse

PROBLEM_NUMBER = "ini5"
SAMPLE_DATASET = """We tried list and we tried dicts also we tried Zen""".splitlines(True)
SAMPLE_OUTPUT = """and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1"""

parser = argparse.ArgumentParser(description=f'Script for Rosalind problem #{PROBLEM_NUMBER}')
parser.add_argument('-d', '--dataset', help='Path to dataset file.')
parser.add_argument('-t', '--testing', action='store_true', help='Test the output of the solution.')

args = parser.parse_args()

path = args.dataset
testing = args.testing

if path:
    with open(path) as f:
        dataset = f.readlines()
else:
    dataset = SAMPLE_DATASET

def solution():
    f"""Solution to Rosalind problem"""
    from collections import Counter
    words = dataset[0].split()
    c = Counter(words)
    return "\n".join([f"{word} {c[word]}" for word in c])

if __name__ == "__main__":
    output = solution()
    if testing:
        try:
            assert SAMPLE_OUTPUT == output
            print('The solution is correct!')
        except:
            print('The soultion is not correct!') 
            print(f'{output} != {SAMPLE_OUTPUT}')
    else:
        print(output)