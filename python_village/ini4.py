#!/usr/bin/env python

"""A simple python script for Rosalind a problem.
"""

__author__ = "Wytamma Wirth"
__license__ = "MIT"
__version__ = "1.0"

import argparse

PROBLEM_NUMBER = "ini4"
SAMPLE_DATASET = """100 200""".splitlines(True)
SAMPLE_OUTPUT = "7500"

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
    numbers = dataset[0].split()
    first = int(numbers[0])
    last= int(numbers[1])
    return str(sum([i for i in range(first, last+1) if i % 2 != 0]))

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

    



