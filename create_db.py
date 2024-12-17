import sqlite3

# �������� ���� ������ � �������
conn = sqlite3.connect('gifts.db')
cursor = conn.cursor()

# �������� �������
cursor.execute('''
CREATE TABLE IF NOT EXISTS gifts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    gift_name TEXT NOT NULL,
    cost INTEGER NOT NULL,
    status TEXT NOT NULL
)
''')

# ���������� ������� �������
gifts_data = [
    ('���� ��������', '�����', 2000, '������'),
    ('����� ���������', '�����', 3000, '�� ������'),
    ('���� ��������', '�����', 1500, '������'),
    ('���� ���������', '�������', 1200, '�� ������'),
    ('������ ���������', '����', 5000, '������'),
    ('����� ����������', '�������', 800, '�� ������'),
    ('������� ����������', '����', 2500, '������'),
    ('����� ��������', '����', 3500, '�� ������'),
    ('��������� �������������', '�����', 4000, '������'),
    ('����� ���������', '��������', 3000, '�� ������')
]

cursor.executemany('''
INSERT INTO gifts (full_name, gift_name, cost, status) VALUES (?, ?, ?, ?)
''', gifts_data)

# ���������� ��������� � �������� ����������
conn.commit()
conn.close()

print("���� ������ ������� � ��������� �������.")