from Bio.Seq import Seq
from Bio.Alphabet import IUPAC, generic_dna
coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)
messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG", IUPAC.unambiguous_rna)
print(repr(messenger_rna))
print(repr(messenger_rna.translate(to_stop=True)))
print(repr(coding_dna.translate(table="Vertebrate Mitochondrial")))
print(repr(coding_dna.translate(table=2, stop_symbol="@")))

yaaX = Seq("GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA" + 
            "GCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGAT" +
            "AATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACAT" +
            "TATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCAT" +
            "AAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA",
            generic_dna)
print(yaaX.translate(table="Bacterial"))
print(yaaX.translate(table="Bacterial", cds=True))