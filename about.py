from flask import Blueprint, render_template

about_bp = Blueprint('about_bp', __name__, 
                    template_folder='templates', 
                    static_folder='static')

@about_bp.route('/')
def index():
  return render_template("about.html")