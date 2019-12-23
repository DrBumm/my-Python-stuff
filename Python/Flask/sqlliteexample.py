import sqlite3, flask
from flask import escape

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE users (name TEXT, addr TEXT)')
#name = "Some"
#addr = "Dude"
#cursor = conn.cursor()
#cursor.execute("SELECT * FROM users")
#rows = cursor.fetchall()
#print(escape(rows[0][0]))
#print(escape(rows[0][1]))
#print(escape(rows[1][0]))
#print(escape(rows[1][1]))
#print(escape(rows[2][0]))
#print(escape(rows[2][1]))
#print(escape(rows[3][0]))
#print(escape(rows[3][1]))
#print(escape(rows[4][0]))
#print(escape(rows[4][1]))
#cursor.execute("INSERT INTO users (name, addr) VALUES (?,?)", (name, addr))
#conn.commit()
conn.close()
