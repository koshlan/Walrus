d = read.delim("SILVA_123_SSURef_Nr99_tax_silva.fasta.rep6.fasta.prefix_table.txt", header = F)
head(d)
sort(table(d$V1)/length(d$V1)*100, decreasing=T)
sort(table(d$V3)/length(d$V3)*100, decreasing=T)
