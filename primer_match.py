# check_for_exact_match.py
# Koshlan Mayer-Blackwell
# July 29, 2015
# This script is written in support of developing V1,V2 amplicon primers, 
# using the dual index approach. I need to find out 2 anticomplementary bases
# before and after my primer sequence. 

# Given a set of seuqences, 
# find where an oligonucleotide will be complementary (fuzzy matching) 
# then find two positions behind that region if they exist. 

# NOTE FOR THIS TO WORK SEQUENCES MUST HAVE "U" in place of "T" and be in all caps (we can add catches for this later)

import argparse
parser = argparse.ArgumentParser(description='subsample_silva.py: \
I wrote this script to get a roughly repressentative sample of sequences \
from the really large 16S sequence database housed at SILVA: \
One can download the following set of sequences as a fasta: \
SILVA_123_SSURef_Nr99_tax_silva.fasta and reduced it to many fewer \
sequences that include coverage of all phylum and lower orders')
parser.add_argument('-in', action="store", dest="fasta_filename")
parser.add_argument('-tokenF', action="store", dest="tokenF", default ="GAGUUUGAUCNUGGCUCAG")
parser.add_argument('-tokenR', action="store", dest="tokenR", default ="UGCUGCCUCCCGUAGGAGU")
r = parser.parse_args()

import difflib
#http://stackoverflow.com/questions/17740833/checking-fuzzy-approximate-substring-existing-in-a-longer-string-in-python (from falsetru)
def matches(large_string, query_string, threshold):
    word = large_string
    s = difflib.SequenceMatcher(None, word, query_string)
    x = s.get_matching_blocks()[0] # look at first block
    i,j,n = x
    if i > 2 and n > 0:
        prefix = "".join(word[i-2:i]).lower()
        match = ''.join(word[i:i+n] for i, j, n in s.get_matching_blocks() if n)
        suffix = ''.join(word[i:i+n+2] for i, j, n in s.get_matching_blocks() if n)[-2:].lower()
        if len(match) / float(len(query_string)) >= threshold:
            return "%s" %(prefix + match + suffix)
    #for i, j, n in s.get_matching_blocks():
      
    
    #match = ''.join(word[i:i+n] for i, j, n in s.get_matching_blocks() if n)
    #if len(match) / float(len(query_string)) >= threshold:
    #    yield match
import sys
from Bio import SeqIO
handle = open(r.fasta_filename, "rU")

ohF = open(r.fasta_filename + ".forward_matches.fasta", "w")
ohR = open(r.fasta_filename + ".reverse_matches.fasta", "w")
ohTable = open(r.fasta_filename + ".prefix_table.txt", "w")

for record in SeqIO.parse(handle, "fasta"):
     large_string = str(record.seq)
     large_stringRC= str(record.seq.reverse_complement())
     mf = matches(large_string, r.tokenF, 0.7)
     mr = matches(large_stringRC, r.tokenR, 0.7)
     if mf and mr:
         ohF.write(">%s\n%s\n" %(record.description, mf))
         ohR.write(">%s\n%s\n" %(record.description, mr))
         ohTable.write( mf[0:2] + "\t" +mf + "\t" + mr[0:2] + "\t" + mr + "\n")
         sys.stdout.write(">%s\n%s\n" %(record.description, mf))
         sys.stdout.write(">%s\n%s\n" %(record.description, mr))
         sys.stdout.write(mf[0:2] + "\t" +mf + "\t" + mr[0:2] + "\t" + mr + "\n")
handle.close()        
ohF.close()
ohR.close()
ohTable.close()  
