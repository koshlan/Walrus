import sqlite3
conn = sqlite3.connect('taxa.db')
c = conn.cursor()
# LIST TABLES
c.execute('''SELECT toy.id my_var1 FROM toy JOIN taxa ON toy.id = taxa.id''')
# close connection
conn.close()

