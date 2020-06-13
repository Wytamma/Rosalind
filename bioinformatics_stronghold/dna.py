from collections import Counter

SAMPLE_DATASET = (
    """AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"""
)
SAMPLE_OUTPUT = """20 12 17 21"""


def solution(dataset: list) -> str:
    c = Counter(dataset[0].strip())  # string is on the first line
    return " ".join(str(c[nt]) for nt in sorted(c))


def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
