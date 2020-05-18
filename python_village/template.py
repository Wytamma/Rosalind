#!/usr/bin/env python

"""A simple python script template for Rosalind problem.
"""

import argparse

PROBLEM_NUMBER = ""
SAMPLE_DATASET = """""".splitlines(True)

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
    f"""Solution to Rosalind problem #{PROBLEM_NUMBER}"""
    pass

if __name__ == "__main__":
    print(solution())
