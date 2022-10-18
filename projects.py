from flask import Blueprint, render_template
from models import Projects

projects_bp = Blueprint('projects_bp', __name__, 
                    template_folder='templates', 
                    static_folder='static')


@projects_bp.route('/')
def index():
  projects = Projects('en')
  return render_template("projects.html", projects=projects.getProjects())

@projects_bp.route('/<project_id>')
def show(project_id):
  projects = Projects('en')
  return render_template("project.html", project=projects.getProject(int(project_id)))