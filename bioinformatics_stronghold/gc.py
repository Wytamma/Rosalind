from pyoinformatics.io import read_fasta

SAMPLE_DATASET = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""
SAMPLE_OUTPUT = """Rosalind_0808
60.919540"""


def solution(dataset: list) -> str:
    sequences = read_fasta(lines=dataset)
    max_gc_seq = max(sequences, key=lambda seq: seq.gc)
    return f"{max_gc_seq.id}\n{max_gc_seq.gc:.6f}"


def test_solution():
    assert solution(SAMPLE_DATASET.splitlines(True)) == SAMPLE_OUTPUT
