from flask import Flask, render_template, url_for

from home import home_bp
from projects import projects_bp
from contact import contact_bp
from about import about_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(projects_bp, url_prefix="/projects")
app.register_blueprint(contact_bp, url_prefix="/contact")
app.register_blueprint(about_bp, url_prefix="/about")
