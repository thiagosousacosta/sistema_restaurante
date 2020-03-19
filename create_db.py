import sqlite3

conn = sqlite3.connect('sistemas.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE Produtos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT, valor real)''')
conn.commit()
conn.close()