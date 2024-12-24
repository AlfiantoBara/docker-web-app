from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi database SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Untuk flash message
db = SQLAlchemy(app)

# Model database untuk buku
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.year}')"

# Buat tabel database jika belum ada
with app.app_context():
    db.create_all()

@app.route('/update_book/<int:id>', methods=['GET', 'POST'])
def update_book(id):
    book = Book.query.get(id)
    
    if not book:
        flash('Book not found!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        # Mengambil data dari form
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        
        # Update data buku
        book.title = title
        book.author = author
        book.year = int(year)

        try:
            db.session.commit()
            flash('Book updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Error: {e}")
            flash('An error occurred while updating the book. Please try again later.', 'error')
            return redirect(url_for('index'))
    
    # Jika metode GET, tampilkan form untuk mengedit buku
    return render_template('edit_book.html', book=book)



# Route untuk halaman utama
@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

# Route untuk menambah buku
@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    year = request.form['year']
    
    if title and author and year:
        new_book = Book(title=title, author=author, year=int(year))
        db.session.add(new_book)
        db.session.commit()
        flash('Book added successfully!', 'success')
    else:
        flash('All fields are required!', 'error')
    return redirect(url_for('index'))

# Route untuk menghapus buku
@app.route('/delete_book/<int:id>', methods=['POST'])
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        flash('Book deleted successfully!', 'success')
    else:
        flash('Book not found!', 'error')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
