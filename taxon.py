__author__ = 'koshlan'




names_file = "/Users/koshlan/taxdmp/names.dmp"
names_D = {}
nodes_file = "/Users/koshlan/taxdmp/nodes.dmp"
nodes_D = {}

with open(names_file, 'r') as names:
    for line in names:
       elements = line.strip().split("|")
       if elements[0] not in nodes_D.keys():
           nodes_D[elements[0]] = elements[1]

with open(nodes_file, 'r') as nodes:
    for line in nodes:
        elements = line.strip().split("|")
        node = elements[0]
        parent = elements[1]
        rank = elements[2]
    nodes_D[node] = {"parent": parent, "rank": rank}


def climb(start, D):
    return( D[start] )


def climb_from_species_to_genus(start, D = names_D):
    node = climb(start, nodes_D) # look in nodes_D for start node
    if node['rank'] == 'species':
        genus_name = D[node['parent']] # genus name is found in dictionary when providing parent key
        return genus_name
    else:
        return "NA"


if __name__ == "__main__":
    start_name = "7"
    parent_name = climb_from_species_to_genus(start_name , names_D)
    print start_name, parent_name

