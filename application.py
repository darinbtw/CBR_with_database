import requests
import sqlite3

url = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
data = url.json()

for key, value in data.items():
    print(f'{key} -> {value}')

Valutes = ['JPY, USD, PLN']

date = data['Date']
name = data['Valute']

conn = sqlite3.connect('cbr_db.db')
cur = conn.cursor()

def create_table(conn, cur):
    cur.execute('''CREATE TABLE IF NOT EXISTS Valutes(
                        id INTEGER PRIMARY KEY,
                        date TEXT NOT NULL,
                        Nominal TEXT NOT NULL,
                        Value float NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# create_table(conn, cur)