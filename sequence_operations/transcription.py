from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)
print(repr(coding_dna))

template_dna = coding_dna.reverse_complement()
print(repr(template_dna))

messenger_rna = coding_dna.transcribe()
print(repr(messenger_rna))
print(repr(template_dna.reverse_complement().transcribe()))
print(repr(messenger_rna.back_transcribe()))