from pyoinformatics.io import read_fasta

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


def slow_solution(dataset: list) -> str:
    sequences = read_fasta(lines=dataset)
    k = 3
    graph = []
    for s in sequences:  # O(n**2)
        for t in sequences:
            if s == t:
                # stop cycling
                continue
            if s[-k:] == t[:k]:
                graph.append((s.id, t.id))
    return "\n".join([f"{edge[0]} {edge[1]}" for edge in graph])


def solution(dataset: list) -> str:
    sequences = read_fasta(lines=dataset)
    k = 3
    edges = []
    nodes = []
    for s in sequences:  # O(n * ( n - 1 ) / 2) == O(n**2), but runs twice as fast
        # check what other nodes in the graph s connects to
        for t in nodes:
            if s.sequence.endswith(t[:k]):
                edges.append((s.id, t.id))
            if t.sequence.endswith(s[:k]):
                edges.append((t.id, s.id))
        # add node to graph
        nodes.append(s)
    return "\n".join([f"{edge[0]} {edge[1]}" for edge in edges])


def test_solution():
    assert slow_solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
    assert set(solution(SAMPLE_DATASET.splitlines(True)).splitlines()) == set(
        SAMPLE_OUTPUT.splitlines()
    )
