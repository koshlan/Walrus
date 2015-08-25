# This builds table for the names
names_file = "/Users/koshlan/taxdmp/names.dmp"
db_location = "/Users/koshlan/PycharmProjects/ContORF/Walrus/taxa.db"

import sqlite3
db = sqlite3.connect(db_location)
c = db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS names (k text, v text)''')
db.commit()

def keys(db):
    cursor = db.cursor()
    return cursor.execute("""SELECT k FROM names""").fetchall()

def get(key, db, default=None):
    cursor = db.cursor()
    result = cursor.execute("""SELECT v FROM names WHERE k = ?""", (key,)).fetchone()
    if result is None:
        return default
    return result[0]

def save(key, value, db):
    cursor = db.cursor()
    cursor.execute("""INSERT INTO names VALUES (?,?)""", (key, value))
    db.commit()

with open(names_file) as file:
    for line in file:
        line = line.strip().split("|")
        save(line[0] , line[1] , db)

