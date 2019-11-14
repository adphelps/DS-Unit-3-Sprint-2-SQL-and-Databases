import sqlite3

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
cur = conn.cursor()

cur.execute('SELECT * FROM review')
cur.fetchall()
cur.execute(
    'SELECT "User Id" FROM review WHERE Nature >= 100 AND Shopping >= 100')
cur.fetchall()
