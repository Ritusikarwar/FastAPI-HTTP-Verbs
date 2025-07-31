import sqlite3 
con = sqlite3.connect(r"D:\mydev\fastapi\users.db") 
cur = con.cursor()
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)
con.close()
