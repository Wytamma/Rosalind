from dataclasses import dataclass

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
    id: str

    def __len__(self) -> int:
        return len(self.sequence)

    @property
    def gc(self) -> float:
        """Return the GC content of the sequence"""
        g = self.sequence.count("G")
        c = self.sequence.count("C")
        return (g + c) / len(self) * 100

    def translate(self) -> str:
        """
        Return the translated sequence.
        *Currently stop signals are ignored.*
        """
        return "".join(codons[self.sequence[i:i+3]] for i in range(0, len(self.sequence), 3) if codons[self.sequence[i:i+3]] != 'Stop')

