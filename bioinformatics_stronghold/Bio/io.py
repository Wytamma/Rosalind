from typing import List
from .seq import Seq


def read_fasta(lines_of_fasta_file: list) -> List[Seq]:
    """Turn the lines of a fasta file into a list of Seq objects"""
    sequences = []
    full_seq = []
    for line in reversed(lines_of_fasta_file):
        if line.startswith(">"):
            sequences.append(Seq(sequence="".join(full_seq[::-1]), id=line.strip()[1:]))
            full_seq = []
            continue
        full_seq.append(line.strip())
    return sequences[::-1]  # return order
