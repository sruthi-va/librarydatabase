import sqlite3

connection = sqlite3.connect('library.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Genres')

cursor.execute('''
CREATE TABLE Genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)
''')

cursor.execute('CREATE INDEX idx_name ON Genres (name)')

genres_data = [
    ('Fiction',),
    ('Non-fiction',),
    ('Science',),
    ('Fantasy',),
    ('Mystery',),
    ('Biography',)
]

cursor.executemany('INSERT INTO Genres (name) VALUES (?)', genres_data)

connection.commit()
connection.close()
