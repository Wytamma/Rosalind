from .Bio import read_fasta

SAMPLE_DATASET = """>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG"""
SAMPLE_OUTPUT = """Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323"""


def solution(dataset: list) -> str:
    sequences = read_fasta(lines=dataset)
    k = 3
    graph = []
    for s in sequences:  # n^2
        for t in sequences:
            if s == t:
                # stop cycling
                continue
            if s[-k:] == t[:k]:
                graph.append((s.id, t.id))
    return "\n".join([f"{edge[0]} {edge[1]}" for edge in graph])


def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
