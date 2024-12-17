from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_gifts():
    # Подключение к базе данных
    conn = sqlite3.connect('gifts.db')
    cursor = conn.cursor()
    
    # Выполнение SQL-запроса
    cursor.execute('SELECT * FROM gifts')
    gifts = cursor.fetchall()
    
    # Закрытие соединения
    conn.close()
    
    return gifts

@app.route('/')
def index():
    gifts = get_gifts()
    return render_template('index.html', gifts=gifts)

if __name__ == '__main__':
    app.run(debug=True)