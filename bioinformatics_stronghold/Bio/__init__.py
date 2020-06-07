from typing import List
from dataclasses import dataclass

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