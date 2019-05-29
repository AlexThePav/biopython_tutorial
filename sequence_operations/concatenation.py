from Bio.Alphabet import IUPAC
from Bio.Alphabet import generic_alphabet
from Bio.Alphabet import generic_nucleotide
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq

# Protein + DNA
protein_seq = Seq("EVRNAK", IUPAC.protein)
dna_seq = Seq("ACGT", IUPAC.unambiguous_dna)

protein_seq.alphabet = generic_alphabet
dna_seq.alphabet = generic_alphabet

print(protein_seq + dna_seq)

# Nucleotide + DNA
nuc_seq = Seq("GATCGATGC", generic_nucleotide)
print(nuc_seq + dna_seq)

# List of DNAs
list_of_seqs = [Seq("ACGT", generic_dna), Seq("AACC", generic_dna), Seq("GGTT", generic_dna)]
# either
concatenated = Seq("", generic_dna)
for s in list_of_seqs:
  concatenated += s
print(concatenated)
# or
print(sum(list_of_seqs, Seq("", generic_dna)))