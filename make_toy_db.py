import sqlite3

# create new db and make connection
conn = sqlite3.connect('taxa.db')
c = conn.cursor()

# create table
c.execute('''CREATE TABLE toy
             (id TEXT, my_var1 TEXT)''')

# insert multiple lines of data
multi_lines =[ ('1','YES'),
               ('116','NO'),
               ('11116','YES')]
c.executemany('INSERT INTO toy VALUES (?,?)', multi_lines)

# save (commit) the changes
conn.commit()

# close connection
conn.close()