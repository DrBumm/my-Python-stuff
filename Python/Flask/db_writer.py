import sqlite3, hashlib

def write_db(name, addr):
#    hashpwd = hashlib.sha512(str.encode(addr))
#    hashpwd.hexdigest()
#    str.decode(addr)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, addr) VALUES (?,?)", (name, addr))
    conn.commit()
    conn.close()
