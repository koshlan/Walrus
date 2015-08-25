# Koshlan Mayer-Blackwell (Aug 23, 2015)
# These methods are used to take fastq files and format them for downstream analysis such as oligotype

def fastq_to_fasta_for_oligotype(fastq_file,
                                 sample,
                                 fix_length = True,
                                 fixed_length = None,
                                 quality_exclude = True,
                                 verbose = True):
    from Bio import SeqIO
    import sys
    class EmptyArgs(StandardError):
        pass

    count = 1 # Counts all records
    length_excluded = 0
    quality_excluded = 0
    passed = 0 # Counts passing records
    for record in SeqIO.parse(fastq_file, "fastq"):
        count = count + 1

        if fix_length:
            if fixed_length == None:
                raise EmptyArgs("fastq_to_fasta_for_oligotype() arg "
                                "<fixed_length> is currently set to default: "
                                "None.\n"
                                "It must be set to integer when fix_length "
                                "= True\n")
            if len(record.seq) != fixed_length:
                length_excluded = length_excluded + 1
                continue


        if quality_exclude:
            # Tries to exclude reads with many low quality base calls
            # usinga arbitrary cut-offs based on analysis by C.Titus Brown's Lab
            # http://angus.readthedocs.org/en/2014/_static/ngs2014-trimming.pdf
            quality =  record.letter_annotations["phred_quality"]
            if (sum([int(x<20) for x in quality]) > 1):
                # if any bases have Phred < 20 exclude
                quality_excluded = quality_excluded + 1
                continue
            if (sum([int(x<25) for x in quality]) > 5):
                # if more than 5 based have Phred < 25
                quality_excluded = quality_excluded + 1
                continue
        passed = passed + 1
        sys.stdout.write(">Sample%s_Read%i\n%s\n"%(sample,count, record.seq))

    if verbose:
        sys.stderr.write("\t# %s was processed by fastq_to_fasta.py\n"%(sample))
        sys.stderr.write("\t# fix_length == %s\n" %(fix_length))
        sys.stderr.write("\t# quality_exclude == %s\n" %(quality_exclude))
        sys.stderr.write("\t# Number of reads failing length check %i \n"
                         %(length_excluded))
        sys.stderr.write("\t# Number of reads failing quality check %i \n"
                         %(quality_excluded))
        sys.stderr.write("\t# Number of reads passing length and quality "
                         "filters: %i of %i \n" %(passed,count))

if __name__ == "__main__":
    example_file = "/Volumes/NO_NAME/Aug2015_HupMiSeq/Stitched/HupAmp1_S10_L001_R1_001.fastq"
    example_length = 334
    sample = "example_sample"
    fastq_to_fasta_for_oligotype(example_file,
                                 sample,
                                 fix_length = True,
                                 fixed_length = 334,
                                 quality_exclude = True)

    # import sys
    # grab =  open(sys.argv[1] , 'r')
    # for item in grab:
    #     #print item
    #     sample = item.strip().split("_")[0]
    #     #print sample
    #     example_file = '/Volumes/NO_NAME/Aug2015_HupMiSeq/Stitched/%s' %(item.strip())
    #     example_length = 334
    #     fastq_to_fasta_for_oligotype(example_file, example_length, sample)
    # grab.close()