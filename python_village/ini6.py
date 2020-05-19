SAMPLE_DATASET = """We tried list and we tried dicts also we tried Zen"""
SAMPLE_OUTPUT = """and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1"""

SAMPLE_OUTPUT = "\n".join(sorted(SAMPLE_OUTPUT.splitlines())) # order doesn't matter

def solution(dataset):
    f"""Solution to Rosalind problem"""
    from collections import Counter
    words = dataset[0].split()
    c = Counter(words)
    return "\n".join(sorted([f"{word} {c[word]}" for word in c]))
