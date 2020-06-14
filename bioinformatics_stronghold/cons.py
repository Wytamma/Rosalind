from .Bio import read_fasta
from collections import Counter

SAMPLE_DATASET = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT"""

SAMPLE_OUTPUT = """ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6"""


def solution(dataset: list) -> str:
    sequences = read_fasta(lines=dataset)
    nucleotides = ["A", "C", "G", "T"]
    all_counts = []
    consensus = ""
    for nts in zip(*sequences):
        nt_counts = Counter(nts)
        consensus += nt_counts.most_common(1)[0][0]
        all_counts.append([str(nt_counts[nt]) for nt in nucleotides])
    profile_matrix = "\n".join(
        [
            f"{nt}: {' '.join(counts)}"
            for nt, counts in zip(nucleotides, zip(*all_counts))
        ]
    )
    return f"{consensus}\n{profile_matrix}"


def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
