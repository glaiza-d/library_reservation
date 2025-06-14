
from flask import Flask, render_template, request, redirect
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def index():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Books;")
    books = cursor.fetchall()
    db.close()
    return render_template('index.html', books=books)

@app.route('/reserve/<int:book_id>', methods=['POST'])
def reserve(book_id):
    user_id = 1  # hardcoded for now
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.callproc('ReserveBook', [user_id, book_id])
        db.commit()
    except Exception as e:
        db.rollback()
        print("Error:", e)
    db.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
