# subset a fasta file unless it is enormous!
# this is a shell of a script that can be improved, but it functional

from Bio import SeqIO
import sys

    # sys.argv[1] : the main fasta file
    # sys.argv[2] : a flat file of sequences accessions to output 

# BUILD THE BIG DICTIONARY OF SEQUENCES
handle = open(sys.argv[1], "rU")
record_dict = SeqIO.to_dict(SeqIO.parse(handle, "fasta"))
handle.close()

# GET THE LIST OF ACCESSSIONS
fh = open(sys.argv[2], "r")
L = [line.strip() for line in fh]
fh.close()

#OUTPUT THE SUBSET TO STDOUT
sequences = [record_dict[x] for x in L]
SeqIO.write(sequences, sys.stdout, "fasta")




