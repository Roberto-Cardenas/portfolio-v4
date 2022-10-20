from wtforms import Form, StringField, TextAreaField, SubmitField, validators

class ContactForm(Form):
  name = StringField('Name', validators=[validators.DataRequired(), validators.length(min=2)])
  email = StringField('Email', validators=[validators.DataRequired(), validators.length(max=80)])
  subject = StringField('Subject', validators=[validators.DataRequired(), validators.length(min=1)])
  message = TextAreaField('Message', validators=[validators.DataRequired(), validators.length(min=1)])
