### Full protocol for design of V1,V2 16S SSU rRNA amplicon primers

#### Dual-Index Primers
The dual-index approach apllied on Illumina MiSeq instrument is well described by a paper: Kozich et al. (2013) in the lab of Patrick Schloss (University of Michigan): (http://www.ncbi.nlm.nih.gov/pubmed/23793624). A full protocol is availabe: (http://www.mothur.org/w/images/0/0c/Wet-lab_MiSeq_SOP.pdf). The protocol describes step that can be taken to extend the approach to other regions of the 16S rRNA gene using alternative amplification primer sequences. The crucial modifications are:

> The only thing to change would be the 16Sf/16Sr sequences and confirm that when combined with the pad sequence that the melting temperature is near 65°C. The link is a 2-nt sequence that is anti-complementary to the known sequences 

A paper by Macintyre et al. (2015) adapt the commonly used 27F and 388R primres used for amplification of the 16S primers targeting the V1, V2 hypervariable regions. (http://www.nature.com/srep/2015/150311/srep08988/full/srep08988.html?utm_source=dlvr.it&utm_medium=tumblr#methods); however the paper does not list the primers used and the corresponding author was on a extended leave in July-August 2015. The method section from Macintyre et al: (2015) does provided the following:

> The V1-V2 hypervariable regions of 16S rRNA genes were amplified for sequencing using a forward and reverse fusion primer. The forward primer was constructed with the Illumina i5 adapter (5′-3′) (AATGATACGGCGACCACCGAGATCTACAC), an 8–10 bp barcode, a primer pad (Forward: TATGGTAATT), and the 28F-GAGTTTGATCNTGGCTCAG primer29. The reverse fusion primer was constructed with (5′-3′) the Illumina i7 adapter (CAAGCAGAAGACGGCATACGAGAT), an 8–10 bp barcode, a primer pad (Reverse: AGTCAGTCAG), and the reverse primer (388R-TGCTGCCTCCCGTAGGAGT)30. Primer pads were designed to ensure the primer pad/primer combination had a melting temperature of 63°C–66°C according to methods developed by the lab of Patrick Schloss (http://www.mothur.org/w/images/0/0c/Wet-lab_MiSeq_SOP.pdf). 

Notably the authors do not describe the anticomplimentary linker region described in the Kozich protocol. This is technically challenging step because it requires checking the nucleotide frequency amoung a large number of 16S sequences in potentially all sequenced microorgansims. W

The general design can be adapted from Macintyre and Kozick but a new link sequence is required:
*AATGATACGGCGACCACCGAGATCTACAC <i5><pad><**link**><16Sf> 
*CAAGCAGAAGACGGCATACGAGAT <i7><pad><**link**><16Sr> 

What follows is a technical description of the code used to determine appropriate linker sequences. 

The starting point of any such analysis is a database of near-full length 16S sequences. On July 25, 2015, 
I downloaded the current non redundant version 123 of the SILVA SSURef database (http://www.arb-silva.de/projects/ssu-ref-nr/). The file name is:
* SILVA_123_SSURef_Nr99_tax_silva.fasta

This is an extremeley large file making a primer search computationally expensive. Instead of using the raw file, I wrote a script for sampling the file in a way that ensures roughly repressentative coverage across taxonomic groups. The script makes use of the fact that the SILVA fasta file includes taxonomic decriptions in the header of each sequences:
> Domain;Kingdom;Phylum;Class;Order;Family;Genus;Species

The basic idea of the subsampler is to walk down the header up to a specified taxonomic level, and only keep the sequence if the header is unique. In this way once a cetertain Genus has been repressented, no futher sequences from that genus will be selected.  To give a sense of why this is useful, consider that there are 4741 sequences repressenting the vibrio genus; whereas when we run the sample we get only 2. 

> grep Vibrio SILVA_123_SSURef_Nr99_tax_silva.fasta | wc -l 

> python subsample_silva.py -in SILVA_123_SSURef_Nr99_tax_silva.fasta -min_length 1480 -max_taxa_depth 6 | grep $">" | grep Vibrio 

#### subsample_silva.py

> grep $">" SILVA_123_SSURef_Nr99_tax_silva.fasta | wc -l 
597607 records

> python subsample_silva.py -in SILVA_123_SSURef_Nr99_tax_silva.fasta -min_length 1480 -max_taxa_depth 6 | grep $">" | wc -l
594 records

We produce a subsample file:

>python subsample_silva.py -in SILVA_123_SSURef_Nr99_tax_silva.fasta -min_length 1480 -max_taxa_depth 6 > SILVA_123_SSURef_Nr99_tax_silva.fasta.rep6.fasta

We can check that we get a few important genus:

* KC342961.1.1489 Bacteria;Chloroflexi;Dehalococcoidia;Dehalococcoidales;Dehalococcoidaceae;Dehalococcoides;Dehalococcoides mccartyi
* U40078.1.1655 Bacteria;Firmicutes;Clostridia;Clostridiales;Peptococcaceae;Desulfitobacterium;Desulfitobacterium hafniense
* U33316.1.1494 Bacteria;Proteobacteria;Deltaproteobacteria;Desulfovibrionales;Desulfovibrionaceae;Desulfovibrio;Desulfovibrio oxyclinae

#### primer_match.py

Next I searched for our primers across the subsample and look at the 2 nucleotides 5' of the primer sequence.

> python primer_match.py -in SILVA_123_SSURef_Nr99_tax_silva.fasta.rep6.fasta

This program has the following input options:

> optional arguments:
  -h, --help          show this help message and exit
  -in FASTA_FILENAME
  -tokenF TOKENF
  -tokenR TOKENR
 
 * -in flag allows user to specify a fasta file of sequences to search
 * -tokenF allows user to specify a forward primer sequence I defaulted it here: 27F "GAGUUUGAUCNUGGCUCAG"
 * -tokenR allows user to specify a reveres primer sequence I defaulted it here: 388R "UGCUGCCUCCCGUAGGAGU" 
 
#####Notes

* tokenR is searched against the reverse complement of the fasta file 
* three output files are created:
  * .prefix_table.txt shows the sequences and the prefix sequences
  * .reverse_matches.fasta (a fasta file with the matching sequence to tokenR)
  * .forward_matches.fasta (a fasta file with the matching sequences to tokenF)


  












 

















