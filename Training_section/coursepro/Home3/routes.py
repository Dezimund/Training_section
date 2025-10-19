from flask import render_template, Blueprint, request, redirect, url_for, flash
from datetime import datetime
from db import db
from models import Book
from forms import BookForm

app = Blueprint('app', __name__)


@app.route('/')
def index():
    book = Book.query.order_by(Book.status).all()
    return render_template('index.html', book=book)


@app.route('/add', methods=['GET', 'POST'])
def add_book_form():
    form = BookForm()
    if form.validate_on_submit():
        date_add_datetime = datetime.combine(form.date_add.data, datetime.min.time())
        date_finish_datetime = None
        if form.date_finish.data:
            date_finish_datetime = datetime.combine(form.date_finish.data, datetime.min.time())

        addbook = Book(
            title=form.title.data,
            author=form.author.data,
            status=form.status.data,
            rating=form.rating.data,
            notes=form.notes.data or "",
            date_add=date_add_datetime,
            date_finish=date_finish_datetime
        )
        db.session.add(addbook)
        db.session.commit()
        flash('Book added successfully!', 'success')
        return redirect(url_for('app.index'))
    return render_template('add_book.html', form=form)


@app.route('/book/<int:id>', methods=['GET'])
def book(id):
    book = Book.query.get_or_404(id)
    return render_template('book_detail.html', book=book)


@app.route('/stats', methods=['GET'])
def stats():
    books = Book.query.order_by(Book.status).all()
    return render_template('stats.html', books=books)