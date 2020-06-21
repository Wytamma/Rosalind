from pyoinformatics.io import Seq

SAMPLE_DATASET = """AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"""
SAMPLE_OUTPUT = """MAMAPRTEINSTRING"""


def solution(dataset: list) -> str:
    seq = Seq(dataset[0].strip(), id="RNA to translate")
    return seq.translate()


def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
