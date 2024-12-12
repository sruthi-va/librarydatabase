from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('genres_index.html')

@app.route('/get_genres')
def get_genres():
    conn = get_db_connection()
    genres = conn.execute('SELECT id, name FROM Genres').fetchall()
    conn.close()
    return jsonify([{'id': genre['id'], 'name': genre['name']} for genre in genres])

if __name__ == '__main__':
    app.run(debug=True)
