#!/usr/bin/env python

"""A simple python script for Rosalind a problem.
"""

__author__ = "Wytamma Wirth"
__license__ = "MIT"
__version__ = "1.0"

import argparse

PROBLEM_NUMBER = "ini3"
SAMPLE_DATASET = """HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102""".splitlines(True)
SAMPLE_OUTPUT = "Humpty Dumpty"

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
    f"""Solution to Rosalind problem"""
    words = dataset[0]
    indices = [int(indice) for indice in dataset[1].split()] 
    word1 = words[indices[0]:indices[1]+1]
    word2 = words[indices[2]:indices[3]+1]
    return f"{word1} {word2}"

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