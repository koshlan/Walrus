# subsample_silva.py
# (c) Koshlan Mayer-Blackwell
# July 29, 2015 

# I wrote this script to get a roughly repressentative sample of sequences 
# from the really large 16S sequence database housed at SILVA:
# One can download the following set of sequences as a fasta
# SILVA_123_SSURef_Nr99_tax_silva.fasta

# The goal of this program is to get a roughly repressentative set of 16S sequences 
# from a really large database. Reducing thousands down to a few hundred, while sampling broadly across the tree of life

# Commandline inputs
# -in allows the user to define the SILVA fasta file to use. 
    # Note it must be formated with taxonomic headers as below (there are no checks):
    #>KC120689.1.1339 Bacteria;Proteobacteria;Gammaproteobacteria;Vibrionales;Vibrionaceae;Photobacterium;uncultured bacterium
# -min_length sets a threshold minimnum length for the sequences to be considered

# The output is directed to stdout and is in the form of a fasta file. 

# Example Execution is as follows:
# python subsample_silva.py -in SILVA_123_SSURef_Nr99_tax_silva.fasta > <OUTPUT> file
# python subsample_silva.py -in SILVA_123_SSURef_Nr99_tax_silva.fasta | grep $">" | wc -l

# Notes: the script rejects uncultured sequences and Eukaryotic sequences

# This block handles the input arguments
import argparse
parser = argparse.ArgumentParser(description='subsample_silva.py: \
I wrote this script to get a roughly repressentative sample of sequences \
from the really large 16S sequence database housed at SILVA: \
One can download the following set of sequences as a fasta: \
SILVA_123_SSURef_Nr99_tax_silva.fasta and reduced it to many fewer \
sequences that include coverage of all phylum and lower orders')
parser.add_argument('-in', action="store", dest="fasta_filename")
parser.add_argument('-min_length', action="store", dest="min_length_threshold", default=1450)
parser.add_argument('-min_taxa_depth', action="store", dest="min_taxa_depth", default=5)
r = parser.parse_args()

from Bio import SeqIO
import sys
handle = open(r.fasta_filename, "rU")

def walk(l):
    item = l.pop(0)
    return(item, l)
    
def is_novel(L, ref):
    if len(L) <= 1:
        return False, "Null"
    else:
        string, L = walk(L)
        if string not in ref:
            return True, string
        else:
            return(is_novel(L,ref))
ref = []
count = 0
min_length_threshold = r.min_length_threshold#1450
for record in SeqIO.parse(handle, "fasta") :
    count = count + 1
    if len(record.seq) > min_length_threshold: 
        #print record.description.split(" ")[1]
        if "uncultured" in record.description.split(" ")[1].split(";"):
            continue
        genus_tree = record.description.split(" ")[1].split(";")[0:r.min_taxa_depth]
        if genus_tree[0] == "Eukaryota":
            continue
            
        a = is_novel(genus_tree, ref)
        #print a
        if a[0]:
            ref.append(a[1])
            #sys.stdout.write(str(record.description.split(" ")[1].split(";")) + "\n")
            sys.stdout.write(">%s\n%s\n" %(record.description, record.seq))
        else:
            continue
    #if count > 10000:
    #    break
handle.close()
