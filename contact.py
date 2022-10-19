from flask import Blueprint, render_template, request, current_app
from flask_mail import Mail, Message

contact_bp = Blueprint('contact_bp', __name__, 
                    template_folder='templates', 
                    static_folder='static')

