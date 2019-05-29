from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
print(repr(my_seq[4:12]))
print(repr(my_seq[4]))
print(my_seq[12])
print(my_seq[::-1])
