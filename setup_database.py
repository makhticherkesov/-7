import sqlite3


connection = sqlite3.connect("medicines.db")


cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS medicines (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    status TEXT NOT NULL
)
''')


medicines_data = [
    ("Ибупрофен", 200, "куплен"),
    ("Активированный уголь", 30, "не куплен"),
    ("Парацетамол", 150, "куплен"),
    ("Супрастин", 450, "не куплен"),
    ("Цетиризин", 350, "куплен"),
    ("Риназолин", 120, "не куплен"),
    ("Лоратадин", 400, "куплен"),
    ("Термометр цифровой", 800, "не куплен"),
    ("Бинт стерильный", 50, "куплен"),
    ("Йод", 20, "не куплен")
]


cursor.executemany('''
INSERT INTO medicines (name, price, status) VALUES (?, ?, ?)
''', medicines_data)

connection.commit()


cursor.execute('SELECT * FROM medicines')
rows = cursor.fetchall()
for row in rows:
    print(row)


connection.close()