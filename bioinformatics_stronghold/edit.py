from pyoinformatics import read_fasta
from pyoinformatics.align import matrix

SAMPLE_DATASET = """>Rosalind_39
PLEASANTLY
>Rosalind_11
MEANLY"""
SAMPLE_OUTPUT = 5

def solution(dataset: list) -> str:
    fasta = read_fasta(lines=dataset)
    Seq1, Seq2 = fasta[0], fasta[1]

    w, h = len(Seq1), len(Seq2)

    # create a empty matrix 
    M = [[0 for x in range(w + 1)] for y in range(h + 1)]

    # pad the first row and col with edit distances from empty strings
    # the distance from '' to HAT is 3 (insertions) 
    #     C A T
    #   0 1 2 3
    # H 1 0 0 0
    # A 2 0 0 0
    # T 3 0 0 0

    M[0] = [i for i in range(len(Seq1)+1)]
    for j in range(len(M)):
        M[j][0] = j

    # calculate the edit distance from the start to each cell
    # i.e. the number of indels or mutations to get there
    # the distance from H to C is 1 (mutation)
    #     C A T
    #   0 1 2 3
    # H 1 1 0 0
    # A 2 0 0 0
    # T 3 0 0 0

    # the distance from H to CA is 2 (1 del 1 mutation)
    #     C A T
    #   0 1 2 3
    # H 1 1 2 0
    # A 2 0 0 0
    # T 3 0 0 0

    # because A and A match there is no extra edit distance 
    # between CA ans HA and H and CA therefore use the last 
    # edit distance
    #     C A T
    #   0 1 2 3
    # H 1 1 2 3
    # A 2 2 1
    # T 3

    for i, ib in enumerate(Seq1, 1):
        for j, jb in enumerate(Seq2, 1):
            if ib == jb:
                edit = M[j-1][i-1]
            else:
                edit = min(
                    M[j -1][i],
                    M[j][i-1], 
                    M[j-1][i-1]) + 1
            M[j][i] = edit
    # M[-1][-1] is the total edit distance from the ends 
    return M[-1][-1]

def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
