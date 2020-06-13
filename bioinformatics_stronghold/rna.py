SAMPLE_DATASET = """GATGGAACTTGACTACGTAAATT"""
SAMPLE_OUTPUT = """GAUGGAACUUGACUACGUAAAUU"""


def solution(dataset):
    string = dataset[0].strip()
    return string.replace("T", "U")

def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT