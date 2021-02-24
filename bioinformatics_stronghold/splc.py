from pyoinformatics import read_fasta

SAMPLE_DATASET = """>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT"""
SAMPLE_OUTPUT = """MVYIADKQHVASREAYGHMFKVCA"""


def solution(dataset: list) -> str:
    sequences = read_fasta(lines=dataset)
    DNA, *introns = sequences
    for intron in introns:
        DNA = DNA.substitute(intron.sequence, "")
    return DNA.transcribe().translate()


def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
