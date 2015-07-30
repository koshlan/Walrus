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
parser.add_argument('-max_taxa_depth', action="store", dest="max_taxa_depth", default=5)
r = parser.parse_args()

# This block opens the fasta file
from Bio import SeqIO
import sys
handle = open(r.fasta_filename, "rU")


# walk

# Args:
    # l is a list 
# Returns
    # a tupel (the first item in the list and and abreviated list)
def walk(l):
    item = l.pop(0)
    return(item, l)

# is_novel 

# This helper function is recursive. It looks at a list and a reference. 
# If the list is greater than 1 in length, it takes a step down the list,
# if the item is novel it returns true; whereas if the item is already in 
# the reference list, it takes another step. The maximum number of steps are specified
# by the length of the list supplied. The user controls this by -min_taxa_depth flag

# Args:
    # L is a list of strings
    # ref is a list of refernce strings 
# Reurns
    # a tuple: (Boolean, String)
        # True if the function finds a novel string, and the string 
        # False if the function does not find a novel string and a "Null" string
def is_novel(L, ref):
    if len(L) <= 1:
        return False, "Null"
    else:
        string, L = walk(L)
        if string not in ref:
            return True, string
        else:
            return(is_novel(L,ref))

ref = [] # This is the blank reference list that will grow as novel taxa are discovered
min_length_threshold = r.min_length_threshold#1450
for record in SeqIO.parse(handle, "fasta") :
    # This rejectes sequences that are not long enough (user specifies min with -min_length flag
    if len(record.seq) > int(min_length_threshold): 
        #This rejects sequences from uncultured organisms
        if record.description.find("uncultured") != -1: 
            continue
        genus_tree = record.description.split(" ")[1].split(";")[0:int(r.max_taxa_depth)]
        #This rejects sequences Eukaryota Kingdom
        if genus_tree[0] == "Eukaryota":
            continue
        # This will return a tuple: (Boolean, String)
        a = is_novel(genus_tree, ref)
        if a[0]:
            ref.append(a[1])
            sys.stdout.write(">%s\n%s\n" %(record.description, record.seq))
        else:
            continue
handle.close()

