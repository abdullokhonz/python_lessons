# import string
#
#
# def DNA_strand(dna):
#     return dna.translate(string.maketrans("ATCG", "TAGC"))
#     # Python 3.4 solution || you don't need to import anything :)
#     # return dna.translate(str.maketrans("ATCG","TAGC"))


def DNA_strand(dna):
    new_dna = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return ''.join(new_dna[i] for i in dna)


print(DNA_strand("GTAT"))
print(DNA_strand("ATTGC"))
