for ACC in A00002 X53307 BB145968 CAA42669 V00181  AH002406  HQ844023
do
   echo -n -e "$ACC\t"
   curl -s "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=${ACC}&rettype=fasta&retmode=xml" |\
   grep TSeq_taxid |\
   cut -d '>' -f 2 |\
   cut -d '<' -f 1 |\
   tr -d "\n"
   echo
 done

ftp://ftp.ncbi.nih.gov/pub/taxonomy/
