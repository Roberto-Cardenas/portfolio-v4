from flask import Blueprint, render_template

contact_bp = Blueprint('contact_bp', __name__, 
                    template_folder='templates', 
                    static_folder='static')

@contact_bp.route('/')
def index():
  return render_template("contact.html")