from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC", IUPAC.unambiguous_dna)

print(str(my_seq))
fasta_format_string = ">Name\n%s\n" % my_seq
print(fasta_format_string)