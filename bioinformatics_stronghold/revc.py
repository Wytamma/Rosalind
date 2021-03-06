SAMPLE_DATASET = """AAAACCCGGT"""
SAMPLE_OUTPUT = """ACCGGGTTTT"""


def solution(dataset: list) -> str:
    complements = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return "".join(complements[nt] for nt in reversed(dataset[0].strip()))


def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
