from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC

my_dna = Seq("AGTACACTGGT", IUPAC.unambiguous_dna)
print(repr(my_dna))
print(my_dna.alphabet)
print(" ")

my_prot = Seq("AGTACACTGGT", IUPAC.protein)
print(repr(my_prot))
print(my_prot.alphabet)

for index, letter in enumerate(my_dna):
  print("%i %s" % (index, letter))
print(len(my_dna))
print(my_dna[10])
print("AAAA".count("AA"))

# overlapping count, GC%
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)
print(len(my_seq))
print(my_seq.count("G"))
print(100 * float(my_seq.count("G") + my_seq.count("C")) / len(my_seq))
print(GC(my_seq))