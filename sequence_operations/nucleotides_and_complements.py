from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
print(repr(my_seq))
print(repr(my_seq.complement()))
print(repr(my_seq.reverse_complement()))
print(repr(my_seq[::-1]))