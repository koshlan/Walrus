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

import pickle
pickle.dump(nodes_D, open("nodes_D.p" , "wb"))

