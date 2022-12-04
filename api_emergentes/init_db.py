import sqlite3

conn = sqlite3.connect('database.db')

with open('schema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute("INSERT INTO company VALUES (1,'compa1','c_api_key1')")
cur.execute("INSERT INTO sensor VALUES (1,1,'sen1','tipo1','algo','s_api_key1')")
cur.execute("INSERT INTO location VALUES (1,1,'loc1','chile','stgo','algo')")

conn.commit()
conn.close()