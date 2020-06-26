import pyoinformatics as pyo


SAMPLE_DATASET = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""
SAMPLE_OUTPUT = """TA"""


def solution(dataset: list) -> str:
    sequences = pyo.io.read_fasta(lines=dataset)
    min_seq = min(sequences, key=len)
    longest_kmer = ""
    for i in range(1, len(min_seq)):
        kmers = min_seq.kmers(i)
        for kmer in kmers:
            if all(kmer.sequence in seq.sequence for seq in sequences) and (
                len(kmer) > len(longest_kmer)
            ):
                longest_kmer = kmer
    return longest_kmer


def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
