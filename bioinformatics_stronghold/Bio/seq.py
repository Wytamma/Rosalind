from dataclasses import dataclass
from typing import Generator
from collections import Counter
from __future__ import annotations

codon_table = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

codons = dict(zip(codon_table.split()[::2], codon_table.split()[1::2]))


@dataclass
class Seq:
    """Class for nucleotide sequences"""

    sequence: str
    id: str = None
    codons: dict = codons

    def __repr__(self):
        return f"Seq({self.Seq[:10]}..., id='{self.id[:15] if self.id}')"
    
    def __str__(self):
        return self.sequence

    def __len__(self) -> int:
        return len(self.sequence)

    def __neg__(self) -> Seq:
        """Negating a Seq object (i.e. !Seq) will return the reverse complement of that sequence"""
        return self.reverse_complement()

    def __add__(self, sequence: Seq) -> Seq:
        """Adding two sequence objects (i.e. Seq1 + Seq2) returns a new Seq object that is the 
        concatenation of the two objects sequences. ID is taken from eh first object""" 
        new_sequence = self.sequence + sequence.sequence
        return Seq(new_sequence, self.id)

    @property
    def gc(self) -> float:
        """Return the GC content of the sequence"""
        g = self.sequence.count("G")
        c = self.sequence.count("C")
        return (g + c) / len(self) * 100

    @property
    def counts(self) -> dict:
        """Return the counts of letters in the sequence"""
        return Counter(self.sequence)

    def kmers(self, n: int, step: int = 1) -> Generator:
        """Return a generator for kmers of length n"""
        return (self.sequence[i : i + n] for i in range(0, len(self.sequence), step))

    def reverse_complement(self) -> Seq:
        complements = {"A": "T", "T": "A", "G": "C", "C": "G"}
        revc = "".join(complements[nt] for nt in reversed(self.sequence))
        return Seq(revc, self.id)

    def transcribe(self) -> Seq:
        return Seq(self.sequence.replace("T", "U"), self.id)

    def translate(self) -> Seq:
        """
        Return the translated sequence.
        *Currently stop signals are ignored.*
        """
        AA = "".join(
            self.codons[self.sequence[i : i + 3]]
            for i in range(0, len(self.sequence), 3)
            if self.codons[self.sequence[i : i + 3]] != "Stop"
        )
        return Seq(AA, self.id)
