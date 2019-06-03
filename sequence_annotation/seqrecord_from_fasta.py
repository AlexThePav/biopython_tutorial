from Bio import SeqIO
record = SeqIO.read("NC_005816.fna", "fasta")
print(repr(record))