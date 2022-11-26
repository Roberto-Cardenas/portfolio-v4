import json

class Projects():
  def __init__(self, language):
    self.projects = self.loadProjects(language)

  def loadProjects(self, language):
    projects = json.load(open('./static/json/projects.json', 'r'))

    return projects[language]

  def getProjects(self):
    return self.projects

  def getProject(self, projectId):
    return self.projects[projectId]
    