from typing import List
from dataclasses import dataclass


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


@dataclass
class Seq:
    """Class for nucleotide sequences"""

    sequence: str
    id: str

    def __len__(self) -> int:
        return len(self.sequence)

    @property
    def gc(self) -> float:
        """Return the GC content of the sequence"""
        g = self.sequence.count("G")
        c = self.sequence.count("C")
        return (g + c) / len(self) * 100


def read_fasta(lines_of_fasta_file: list) -> List[Seq]:
    """Turn the lines of a fasta file into a list of Seq objects"""
    sequences = []
    full_seq = ""
    for line in reversed(lines_of_fasta_file):
        if line.startswith(">"):
            sequences.append(Seq(sequence=full_seq, id=line.strip()[1:]))
            full_seq = ""
            continue
        full_seq += line.strip()
    return sequences


def solution(dataset: list) -> str:
    sequences = read_fasta(dataset)
    max_gc_seq = max(sequences, key=lambda seq: seq.gc)
    return f"{max_gc_seq.id}\n{max_gc_seq.gc:.6f}"
