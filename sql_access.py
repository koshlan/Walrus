__author__ = 'koshlan'
#TO DEAL WITH MONSTER FILES WE CAN UES A RELATIONAL DATABASE HELD LOCALLY
import sqlite3
conn = sqlite3.connect('taxa.db')
c = conn.cursor()
# create table
c.execute('''CREATE TABLE taxa
             (id TEXT, my_var1 TEXT)''')
# insert multiple lines of data
def clean_up(x):
    (a,b) = x.strip().split("\t")
    return (a,b)
counter =  0
multi_lines = []
with open("/Users/koshlan/gi_taxid_nucl.dmp") as f:
    for line in f:
        counter += 1
        if counter < 100000:
            a,b = line.strip().split("\t")
            multi_lines.append((a,b))
        else:
            c.executemany('INSERT INTO taxa VALUES (?,?)', multi_lines)
            conn.commit()
            multi_lines = [ ]
            counter = 0
# close connection
conn.close()
