SAMPLE_DATASET = """We tried list and we tried dicts also we tried Zen""".splitlines(True)
SAMPLE_OUTPUT = """and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1"""

def solution():
    f"""Solution to Rosalind problem"""
    from collections import Counter
    words = dataset[0].split()
    c = Counter(words)
    return "\n".join([f"{word} {c[word]}" for word in c])
