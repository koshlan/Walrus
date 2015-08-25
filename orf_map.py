__author__ = 'koshlan'

def produce_orf_genus_dictionary(filename, delim = "\t"):
    '''
    given a key value pair build a dictionary of keyed on orf to predicted
    :param filename:
    :param delim:
    :return:
    '''
    fh = open(filename, "r")
    D = {}
    for line in fh:
        line = line.strip().split(delim)
        D[line[0]] = line[1]
    D["NA"] = "NA"
    return(D)


def orf_to_contig(orf_key, dictionary):
    '''
    :param orf_key:
    :param dictionary:
    :return contig_name: name of the contig containing the orf_string
    :except KeyError: if the the orf is not in the dictionary return "NA"
    '''
    try:
        congtig_name = dictionary[orf_key]
        return(contig_name)
    except KeyError:
        return("NA")

def orf_to_genus(orf_key, dictionary):
    '''
    :param orf_key:
    :param dictionary:
    :return genus_name: name of the contig containing the orf_string
    :except KeyError: if the the orf is not in the dictionary return "NA"
    '''
    try:
        genus_name = dictionary[orf_key]
        return(genus_name)
    except KeyError:
        return("NA")

def contig_to_orfs(contig_key, dictionary):
    '''
    :param contig_key:
    :param dictionary:
    :return orf_list: name of the contig containing the orf_string
    :except KeyError: if the the orf is not in the dictionary, return ["NA"]
    '''
    try:
        orf_list = dictionary[contig_key]
        return(orf_list)
    except KeyError:
        return(["NA"])

def contig_to_genus(contig_key, contig_to_orf_dict, orf_to_genus_dict ):
    orf_list = contig_to_orfs(contig_key, contig_to_orf_dict)
    genera_list = [orf_to_genus(x, orf_to_genus_dict) for x in orf_list]
    D = {contig_key : genera_list}
    return(D)

if __name__ == "__main__":
    # This is a really simple example. We nee to know the predicted genus of this contig
    # based on anotated genes comprising it. This example is for one contig.
    # The strength of this is that we can loop over very large files
    # using the same dictionaries in memory

    my_contig = "NODE_1001_length_9403_cov_6.17598_ID_32345614"

    # (1) I need to parse the prokka.tbl or unpickle previously generated dictionaries
    from prokka_table_parse import prokka_table_parse
    my_prokka_table = "examples/inputs/EV5L_sample.tbl"

        # prokka_table_parse()
    (orf_to_contig_dict, contig_to_orf_dict) = prokka_table_parse(my_prokka_table,
                                                                  return_dictionaries = True)

    # (2) produce_orf_genus_dictionary()
    # I assume that I have a key value pair orf, genus. This will likely be done
    # with a blast search, the file here is a toy only for this example

    genus_example_file = "examples/inputs/genus_sample.txt"
    orf_to_genus_dict = produce_orf_genus_dictionary(filename = genus_example_file, delim = "\t")

    # (3) contig_to_genus() with the appropriate dictionaries provides a list of genus associated
    # with each org on that contig
    print contig_to_genus(my_contig, contig_to_orf_dict, orf_to_genus_dict)



