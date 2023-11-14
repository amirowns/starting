def DNA_strand(dna):
    # return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    uhh = str.maketrans("ATCG","TAGC")
    return dna.translate(uhh)

# print(DNA_strand("CGGGTACA"))

def complement_dna(dna_str):
    complement = ""
    for base in dna_str:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"
    return complement

print(complement_dna("CGGGTACA")) # GCCCATGT
