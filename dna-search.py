# DNA search implemented in python

from typing import Tuple,List
from enum import IntEnum

Nucleotide: IntEnum = IntEnum(Nucleotide('A','C','G','T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

def str_to_gene(s:str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i+2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene

my_gene: Gene = str_to_gene(gene_str)

# linear search

def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if key_codon == codon
        return True
    return False


# binary search

def binary_contains(gene: Gene, key_cordon: Cordon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < key_cordon:
            low = mid + 1
        elif gene[mid] > key_cordon:
            high = mid - 1
        else:
            return True
    return False


