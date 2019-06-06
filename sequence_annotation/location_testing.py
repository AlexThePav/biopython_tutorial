from Bio import SeqIO
my_snp = 4350
record = SeqIO.read("NC_005816.gb", "genbank")
for feature in record.features:
  if my_snp in feature:
    print("%s %s" % (feature.type, feature.qualifiers.get("db_xref")))