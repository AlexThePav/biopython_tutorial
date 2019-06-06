from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
example_parent = Seq("ACCGAGACGGCAAAGGCTAGCATAGGTATGAGACTTCCTTCCTGCCAGTGCTGAGGAACTGGGAGCCTAC")
example_feature = SeqFeature(FeatureLocation(5, 18), type="gene", strand=-1)
feature_seq = example_parent[example_feature.location.start:example_feature.location.end].reverse_complement()
print(feature_seq)