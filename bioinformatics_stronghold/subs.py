SAMPLE_DATASET = """GATATATGCATATACTT
ATAT
"""
SAMPLE_OUTPUT = """2 4 10"""


def kmer_generator(string, n):
    """returns a generator for kmers of length n"""
    return (string[i : i + n] for i in range(0, len(string)))


def solution(dataset: list) -> str:
    s, t = map(lambda x: x.strip(), dataset)  # clean
    locs = [
        str(i) for i, kmer in enumerate(kmer_generator(s, len(t)), 1) if kmer == t
    ]  # process
    return " ".join(locs)  # report
