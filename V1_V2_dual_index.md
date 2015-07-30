### Full protocol for design of V1,V2 16S SSU rRNA amplicon primers

#### Dual-Index Primers

The dual-index approach apllied on Illumina MiSeq instrument is well described by a paper: Kozich et al. (2013) in the lab of Patrick Schloss (University of Michigan): (http://www.ncbi.nlm.nih.gov/pubmed/23793624). A full protocol is availabe: (http://www.mothur.org/w/images/0/0c/Wet-lab_MiSeq_SOP.pdf). The protocol describes step that can be taken to extend the approach to other regions of the 16S rRNA gene using alternative amplification primer sequences. The crucial modifications are:

> The only thing to change would be the 16Sf/16Sr sequences and confirm that when combined with the pad sequence that the melting temperature is near 65°C. The link is a 2-nt sequence that is anti-complementary to the known sequences 



A paper by Macintyre et al. (2015) adapt the commonly used 27F and 388R primres used for amplification of the 16S primers targeting the V1, V2 hypervariable regions. (http://www.nature.com/srep/2015/150311/srep08988/full/srep08988.html?utm_source=dlvr.it&utm_medium=tumblr#methods); however the paper does not list the primers used and the corresponding author was on a extended leave in July-August 2015. The method section from Macintyre et al: (2015) does provided the following:

> The V1-V2 hypervariable regions of 16S rRNA genes were amplified for sequencing using a forward and reverse fusion primer. The forward primer was constructed with the Illumina i5 adapter (5′-3′) (AATGATACGGCGACCACCGAGATCTACAC), an 8–10 bp barcode, a primer pad (Forward: TATGGTAATT), and the 28F-GAGTTTGATCNTGGCTCAG primer29. The reverse fusion primer was constructed with (5′-3′) the Illumina i7 adapter (CAAGCAGAAGACGGCATACGAGAT), an 8–10 bp barcode, a primer pad (Reverse: AGTCAGTCAG), and the reverse primer (388R-TGCTGCCTCCCGTAGGAGT)30. Primer pads were designed to ensure the primer pad/primer combination had a melting temperature of 63°C–66°C according to methods developed by the lab of Patrick Schloss (http://www.mothur.org/w/images/0/0c/Wet-lab_MiSeq_SOP.pdf). 

Notably the authors do not describe the anticomplimentary linker region described in the Kozich protocol. This is technically challenging step because it requires checking the nucleotide frequency amoung a large number of 16S sequences in potentially all sequenced microorgansims. What follows is a technical description of the code used to determine appropriate linker sequences:

The general design can be adapted from Macintyre and Kozick but a new link sequence is required:
AATGATACGGCGACCACCGAGATCTACAC <i5><pad><**link**><16Sf> 
CAAGCAGAAGACGGCATACGAGAT <i7><pad><**link**><16Sr> 

















