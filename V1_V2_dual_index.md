### Full protocol for design of V1,V2 16S SSU rRNA amplicon primers

#### Dual-Index Primers

The dual-index approach apllied on Illumina MiSeq instrument is well described by a paper: Kozich et al. (2013) in the lab of Patrick Schloss (University of Michigan): (http://www.ncbi.nlm.nih.gov/pubmed/23793624). A full protocol is availabe: (http://www.mothur.org/w/images/0/0c/Wet-lab_MiSeq_SOP.pdf). The protocol describes step that can be taken to extend the approach to other regions of the 16S rRNA gene using alternative amplification primer sequences. The crucial modifications are:

> The only thing to change would be the 16Sf/16Sr sequences and confirm that when combined with the pad sequence that the melting temperature is near 65°C. The link is a 2-nt sequence that is anti-complementary to the known sequences 

A paper by Macintyre et al. (2015) adapt the commonly used 27F and 388R primres used for amplification of the 16S primers targeting the V1, V2 hypervariable regions. (http://www.nature.com/srep/2015/150311/srep08988/full/srep08988.html?utm_source=dlvr.it&utm_medium=tumblr#methods); however the paper does not list the primers used and the corresponding author was on a extended leave in July-August 2015. The method section from Macintyre et al: (2015) does provided the following:

> The V1-V2 hypervariable regions of 16S rRNA genes were amplified for sequencing using a forward and reverse fusion primer. The forward primer was constructed with the Illumina i5 adapter (5′-3′) (AATGATACGGCGACCACCGAGATCTACAC), an 8–10 bp barcode, a primer pad (Forward: TATGGTAATT), and the 28F-GAGTTTGATCNTGGCTCAG primer29. The reverse fusion primer was constructed with (5′-3′) the Illumina i7 adapter (CAAGCAGAAGACGGCATACGAGAT), an 8–10 bp barcode, a primer pad (Reverse: AGTCAGTCAG), and the reverse primer (388R-TGCTGCCTCCCGTAGGAGT)30. Primer pads were designed to ensure the primer pad/primer combination had a melting temperature of 63°C–66°C according to methods developed by the lab of Patrick Schloss (http://www.mothur.org/w/images/0/0c/Wet-lab_MiSeq_SOP.pdf). Amplifications were performed in 25 μl reactions with Qiagen HotStar Taq master mix (Qiagen Inc, Valencia, California), 1 μl of each 5 uM primer, and 1 μl of template. Reactions were performed on ABI Veriti thermocyclers (Applied Biosytems, Carlsbad, California) under the following thermal profile: 95°C for 5 min, then 35 cycles of 94°C for 30 sec, 54°C for 40 sec, 72°C for 1 min, followed by one cycle of 72°C for 10 min and 4°C hold. Amplification products were visualized with eGels (Life Technologies, Grand Island, New York). Products were then pooled equimolar and each pool was size selected in two rounds using Agencourt AMPure XP (BeckmanCoulter, Indianapolis, Indiana) in a 0.7 ratio for both rounds. Size selected pools were then quantified using the Quibit 2.0 Fluorometer (Life Technologies) and loaded on an Illumina MiSeq (Illumina, Inc. San Diego, California) 2 × 300 flow cell at 10 pM. All sequencing was performed at Research and Testing Laboratory (Lubbock, TX, USA).

Notably the authors do not describe the anticomplimentary linker region described in the Kozich protocol.  
















