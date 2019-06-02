from Bio.Seq import Seq
from Bio.Seq import MutableSeq
from Bio.Alphabet import IUPAC

my_seq = MutableSeq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA", IUPAC.unambiguous_dna)
# my_seq[6] = "C"
my_seq.remove("T")
my_seq.reverse()
print(repr(my_seq))
non_mutable_seq = my_seq.toseq()