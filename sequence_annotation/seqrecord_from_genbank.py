from Bio import SeqIO
record = SeqIO.read("NC_005816.gb", "genbank")
print(repr(record))
print(record.id)
print(record.name)
print(record.description)
print(record.letter_annotations)
for annotation in record.annotations:
  print(annotation)
print(record.dbxrefs)
for feature in record.features:
  print(feature)