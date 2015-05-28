def prokka_table_parse(filename, d1_name = "D.p", d2_name = "Dr.p" , return_dictionaries = False):
    '''
    Koshlan Mayer-Blackwell
    May 28, 2015

    prokka_table_parse()

    Background: Prokka produces a .tbl file which can be parsed to determine
                 which predicted ORFs are on which contigs.
                 use this function to generate dictoinaries linking
                    (A) orfs to contigs
                    (B) contigs to a list of orfs

    Parameters:
        filename - to a Prokka .tbl
        d1_name  - the name to pickle dictionary
            {orf1: Contig, orf2: Contig, .. }
        d2_name  - the name to pickle dictionary
            {Contig :[orf1, orf2], Contig2 :[orf5, orf7] ..}
        return_dictionaries (Defaults to False)
            if true will return dictionaries direction on function call
            e.g.  usage d1, d2 <- prokka_table_parse()

     Returns:
        if return_dictionaries == True)
        D
        Dr
        always serializes

     Raises:
        ValueError if filename does not end in .tbl

     Example Usage:

     Explanation of Code:
       Block (1): reads file line by line finding contig nodes
               and lines containing pattern "(PROKKA_[0-9]+)"
               Produces dictionary where wach unique prokka id
               is a key pointing to the contig node which contains it

       Block (2): reverses the dictionary
               A second dictionary has nodes as keys and
               list of all contigs contained

       Block (3): uses pickle to serialize the 2 dictionaries

       Block (4): Optional on return_dictionaries = True
                can return dictionaries
    '''# (1)
    import re
    import pickle
    if filename.split(".")[-1] != "tbl":
       raise ValueError('This function excepts Prokka.tbl extension files only')
    fh = open(filename, 'r')
    D = {}
    for line in fh:
        if line.startswith(">"):
            node = line.replace(">Feature ", "").strip()
        else:
            r = re.search("(PROKKA_[0-9]+)", line)
            if r:
                D[r.group(1)] = node
            else:
                continue
    # (2)
    Dr = {}
    for k in D.keys():
        node = D[k]
        if node not in Dr.keys():
            Dr[node] = []
        Dr[node].append(k)
    # (3)
    pickle.dump( D, open( d1_name, "wb" ))
    pickle.dump( Dr, open( d2_name , "wb" ))
    # (4)
    if return_dictionaries:
        return((D,Dr))

if __name__ == "__main__":
    # python prokka_table_parse.py examples/inputs/EV5L_full.tbl.txt
    import sys
    prokka_table_parse(sys.argv[1])
