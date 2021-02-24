from pyoinformatics.io import read_fasta

SAMPLE_DATASET = """>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA"""
SAMPLE_OUTPUT = """3 4 5"""  # changed for multiple soultions

def solution(dataset: list) -> str:
    sequences = read_fasta(lines=dataset)
    DNA = sequences[0]
    subsequence = sequences[1]
    indices = []
    offest = 0

    for base in subsequence:
        loc = DNA[offest:].find(base)
        offest = loc + offest + 1
        indices.append(str(offest))
    
    # sanity check
    for i, idx in enumerate(indices):
        try:
            assert subsequence[i] == DNA[int(idx)-1]
        except:
            print (f"{subsequence[i]} != {DNA[int(idx)-1]} at {idx}")

    return " ".join(indices)

def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT