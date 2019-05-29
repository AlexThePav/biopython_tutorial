from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from Bio.Alphabet import IUPAC

dna_seq = Seq("acgtACGT", generic_dna)
print(repr(dna_seq))
print(dna_seq.upper())
print(dna_seq.lower())
print("TAC" in dna_seq)
print("TAC" in dna_seq.upper())

strict_dna_seq = Seq("ACGT", IUPAC.unambiguous_dna)
print(repr(strict_dna_seq))
print(repr(strict_dna_seq.lower()))