from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    bookID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    genre = db.Column(db.String)
    isbnID = db.Column(db.String, unique=True, nullable=False)
    numAvail = db.Column(db.Integer, default=0)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('library_index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    isbnID = request.form['isbnID']
    numAvail = request.form['numAvail']
    
    new_book = Book(title=title, author=author, genre=genre, isbnID=isbnID, numAvail=numAvail)
    db.session.add(new_book)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/edit/<int:bookID>', methods=['GET', 'POST'])
def edit_book(bookID):
    book = Book.query.get_or_404(bookID)
    
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.genre = request.form['genre']
        book.isbnID = request.form['isbnID']
        book.numAvail = request.form['numAvail']
        
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('edit.html', book=book)

@app.route('/delete/<int:bookID>')
def delete_book(bookID):
    book = Book.query.get_or_404(bookID)
    db.session.delete(book)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
