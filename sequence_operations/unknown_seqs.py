from Bio.Seq import UnknownSeq
from Bio.Alphabet import IUPAC

unk = UnknownSeq(20, alphabet=IUPAC.ambiguous_dna)
unk.complement()
unk.reverse_complement()
unk_rna = unk.transcribe()
print(unk_rna)
unk_protein = unk.translate()
print(unk_protein)