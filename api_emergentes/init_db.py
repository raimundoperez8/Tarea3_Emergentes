import sqlite3

conn = sqlite3.connect('database.db')

with open('schema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute("INSERT INTO admin VALUES (1,'admin','password','a_api_key1')")


cur.execute("INSERT INTO company VALUES (1,'compa1','c_api_key1')")
cur.execute("INSERT INTO company VALUES (2,'compa2','c_api_key2')")


cur.execute("INSERT INTO location VALUES (1,1,'loc1','chile','stgo','algo')")
cur.execute("INSERT INTO location VALUES (1,2,'loc2','chile','stgo2','meta_texto')")
cur.execute("INSERT INTO location VALUES (2,3,'lugar','uruguay','montevid','mucho texto')")


cur.execute("INSERT INTO sensor VALUES (1,1,'sen1','tipo1','algo','s_api_key1')")
cur.execute("INSERT INTO sensor VALUES (1,2,'sen2','tipo1','algo, pero 2','s_api_key2')")
cur.execute("INSERT INTO sensor VALUES (2,3,'sen3','tipo1','algo, pero 3, creo','s_api_key3')")



conn.commit()
conn.close()