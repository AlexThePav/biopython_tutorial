from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_dna_by_name["Standard"] # id: 1
mito_table = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"] # id: 2

# print(standard_table)
# print(mito_table)

print(standard_table.stop_codons)
print(mito_table.start_codons)
print(mito_table.forward_table["ACG"])