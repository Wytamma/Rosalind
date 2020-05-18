#!/usr/bin/env python

"""A simple python script template for Rosalind problem.
"""

import argparse

PROBLEM_NUMBER = "ini3"
SAMPLE_DATASET = """HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102""".splitlines(True)

parser = argparse.ArgumentParser(description=f'Script for Rosalind problem #{PROBLEM_NUMBER}')
parser.add_argument('--dataset', help='path to dataset file.')
args = parser.parse_args()

dataset_path = args.dataset

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
    print(solution())
