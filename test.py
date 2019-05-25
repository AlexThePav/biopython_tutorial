import Bio
from Bio.Seq import Seq

print(Bio.__version__)
my_seq = Seq("AGTACACTGGT")
# my_seq
print(my_seq)
print(my_seq.alphabet)
print(my_seq.complement())
print(my_seq.reverse_complement())