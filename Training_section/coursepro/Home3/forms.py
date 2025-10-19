from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Optional


class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=20)])
    author = StringField('Author', validators=[DataRequired(), Length(max=20)])
    status = SelectField('Status', choices=[
        ('reading', 'Reading'),
        ('read', 'Read'),
        ('to-read', 'To Read')
    ], validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
    notes = TextAreaField('Notes', validators=[Optional(), Length(max=200)])
    date_add = DateField('Add Date', format='%Y-%m-%d', validators=[DataRequired()])
    date_finish = DateField('Finish Date', format='%Y-%m-%d', validators=[Optional()])