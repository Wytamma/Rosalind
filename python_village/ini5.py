#!/usr/bin/env python

"""A simple python script for Rosalind a problem.
"""

__author__ = "Wytamma Wirth"
__license__ = "MIT"
__version__ = "1.0"

import argparse

PROBLEM_NUMBER = "ini5"
SAMPLE_DATASET = """Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat""".splitlines(True)
SAMPLE_OUTPUT = """Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat"""

parser = argparse.ArgumentParser(description=f'Script for Rosalind problem #{PROBLEM_NUMBER}')
parser.add_argument('-d', '--dataset', help='Path to dataset file.')
parser.add_argument('-t', '--testing', action='store_true', help='Test the output of the solution.')

args = parser.parse_args()

dataset_path = args.dataset
testing = args.testing

if dataset_path:
    with open(dataset_path) as f:
        dataset = f.readlines()
else:
    dataset = SAMPLE_DATASET

def solution():
    f"""Solution to Rosalind problem #{PROBLEM_NUMBER}"""
    return "".join([line for i, line in enumerate(dataset, 1) if i % 2 == 0])

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