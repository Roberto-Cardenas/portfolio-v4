from flask import Flask, render_template, url_for, request, redirect
from flask_mail import Mail, Message
from forms import ContactForm
from home import home_bp
from projects import projects_bp
from about import about_bp

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'robertocardenasportfolio@gmail.com'
app.config['MAIL_PASSWORD'] = 'okuyaxkjvlrqqsvh'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

app.register_blueprint(home_bp)
app.register_blueprint(projects_bp, url_prefix="/projects")
app.register_blueprint(about_bp, url_prefix="/about")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm(request.form)
  if request.method == 'POST' and form.validate():
    msg = Message(form.subject.data, 
                  sender='robertocardenasportfolio@gmail.com', 
                  recipients=['robertocardenas@berkeley.edu'])
    msg.body = "Email: " + form.email.data + ". Name: " + form.name.data + ". Message: " + form.message.data
    mail.send(msg)
    return redirect(url_for('contact'))

  return render_template("contact.html", form=form)
