from pyoinformatics.io import read_fasta

SAMPLE_DATASET = """>Rosalind_23
AACCTTGG
>Rosalind_64
ACACTGTGA"""
SAMPLE_OUTPUT = """AACTTG"""


def solution(dataset: list) -> str:
    fasta = read_fasta(lines=dataset)
    Seq1, Seq2 = fasta[0], fasta[1]
    w, h = len(Seq1), len(Seq2)
    Matrix = [[0 for x in range(w + 1)] for y in range(h + 1)]

    for i, ibase in enumerate(Seq1, 1):
        for j, jbase in enumerate(Seq2, 1):
            if ibase == jbase:
                Matrix[j][i] = Matrix[j - 1][i - 1] + 1
            else:
                Matrix[j][i] = max(Matrix[j - 1][i], Matrix[j][i - 1])

    # remove zeros
    Matrix = [M[1:] for M in Matrix[1:]]

    # print(" ", " ".join([nt for nt in Seq1]))
    # for i, b in enumerate(Seq2):
    #     print(b, " ".join([str(s) for s in Matrix[i]]))

    # len(LCS) == Matrix[len(Seq2) - 1][len(Seq1) - 1]

    i, j = len(Seq1) - 1, len(Seq2) - 1
    LCS = []
    while i > -1 and j > -1:
        if Seq1[i] == Seq2[j]:
            LCS.append(Seq1[i])
            j -= 1
            i -= 1
        elif Matrix[j][i - 1] == Matrix[j][i]:
            i -= 1
        elif Matrix[j - 1][i] == Matrix[j][i]:
            j -= 1

    return "".join(LCS)[::-1]


def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
