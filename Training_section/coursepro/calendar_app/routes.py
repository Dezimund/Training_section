from flask import render_template, Blueprint, request, redirect, url_for, flash
from datetime import datetime
from db_config import db
from models import Event
from forms import EventForm

app = Blueprint('app', __name__)

@app.route('/')
def index():
    events = Event.query.order_by(Event.date).all()
    return render_template('index.html', events=events)

@app.route('/add', methods=['GET', 'POST'])
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        new_event = Event(
            title=form.title.data,
            description=form.description.data,
            date=form.date.data
        )
        db.session.add(new_event)
        db.session.commit()
        flash('Event added successfully!','success')
        return redirect(url_for('app.index'))
    else:
        flash('Incorrect input!','warning')
    return render_template('add_event.html', form=form)

@app.route('/delete/<int:id>')
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    flash('Event deleted successfully!','success')
    return redirect(url_for('app.index'))
