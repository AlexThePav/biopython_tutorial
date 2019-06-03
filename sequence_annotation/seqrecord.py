from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
# print(help(SeqRecord))

simple_seq = Seq("GATC")
simple_seq_r = SeqRecord(simple_seq, id="AC12345")
simple_seq_r.annotations["evidence"] = "None. I just made it up."
simple_seq_r.description = "Made up sequence I wish I could write a paper about"
simple_seq_r.letter_annotations["phred_quality"] = [40, 40, 38, 30]

print(repr(simple_seq))
print(repr(simple_seq_r))
print(simple_seq_r.annotations)
print(simple_seq_r.letter_annotations)