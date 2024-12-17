import sqlite3

# Создание базы данных и таблицы
conn = sqlite3.connect('gifts.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS gifts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    gift_name TEXT NOT NULL,
    cost INTEGER NOT NULL,
    status TEXT NOT NULL
)
''')

# Заполнение таблицы данными
gifts_data = [
    ('Иван Иванович', 'Санки', 2000, 'куплен'),
    ('Ирина Сергеевна', 'Цветы', 3000, 'не куплен'),
    ('Петр Петрович', 'Книга', 1500, 'куплен'),
    ('Анна Андреевна', 'Игрушка', 1200, 'не куплен'),
    ('Сергей Сергеевич', 'Часы', 5000, 'куплен'),
    ('Елена Викторовна', 'Конфеты', 800, 'не куплен'),
    ('Дмитрий Дмитриевич', 'Вино', 2500, 'куплен'),
    ('Мария Ивановна', 'Плед', 3500, 'не куплен'),
    ('Александр Александрович', 'Сумка', 4000, 'куплен'),
    ('Ольга Сергеевна', 'Наушники', 3000, 'не куплен')
]

cursor.executemany('''
INSERT INTO gifts (full_name, gift_name, cost, status) VALUES (?, ?, ?, ?)
''', gifts_data)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("База данных создана и заполнена данными.")