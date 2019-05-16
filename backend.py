import sqlite3
from flask import Flask, jsonify, request, current_app
import csv

app = Flask(__name__)

def connect():
    try:
        conn = sqlite3.connect('movies.db')
        cur = conn.cursor()
        return conn, cur
    except sqlite3.Error as e:
        print(e, 'Not connected!')

def create_table(): #todo- gives syntax error- handle it?
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='movies';")
        result = cursor.fetchone()
        if result[0] == 1:
            return
        cursor.execute('CREATE TABLE if not exists movies (id TEXT PRIMARY KEY,title TEXT,genre TEXT);')
        conn.commit()
        conn.close()
        insert_from_csv()
    except sqlite3.Error as e:
        print(e)

def insert(id, title, genre):
    try:
        conn, cursor = connect()
        if '|' in genre:
            genre = genre.split('|')[0]
        cursor.execute('insert into movies(id, title, genre) VALUES(?,?,?);', (id, title, genre))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)

def insert_from_csv():
    with open('movies.csv', 'r', encoding="utf8") as file:
        movies = csv.reader(file, delimiter=',')
        for index,row in enumerate(movies):
            if index == 0:
                continue
            insert(row[0], row[1], row[2])

@app.route('/', methods=['GET','POST'])
def view_all():
    conn, cursor = connect()
    with conn:
        cursor.execute('select * from movies;')
        rows = cursor.fetchall()
        return rows

def delete(id, title, genre):
    conn, cursor = connect()
    with conn:
        cursor.execute('delete from movies where id=? and title=? and genre=?;', (id, title, genre))
        conn.commit()

def search(id, title, genre):
    conn, cursor = connect()
    with conn:
        cursor.execute('select * from movies where id=? or title=? or genre=?;', (id, title, genre)) #todo- fix query!!
        rows = cursor.fetchall()
        return rows

def update(id, title, genre):
    conn, cursor = connect()
    with conn:
        cursor.execute('update movies set title=? and genre=? where id=?;', (id, title, genre)) # todo: fix query- for every field
        conn.commit()

def check(movie):
    conn, cursor = connect()
    with conn:
        cursor.execute('select * from movies where id=? or title=? or genre=?;', (movie[0]+1, movie[0]+1, movie[0]+1))
        conn.commit()
        rows = cursor.fetchall()
        return rows

#request.form['username']

if __name__ == '__main__':  # run the server
    with app.app_context():
        # within this block, current_app points to app.
        print(current_app.name)
    app.run(debug=True)
