class Projects():
  def __init__(self, language):
    self.projects = self.loadProjects(language)

  def loadProjects(self, language):
    projects = {
      'en': [
        {
          'title': 'CZ Waste Website',
          'shortDescription': 'Waste Information Website for Casa Zimbabwe, a student housing unit that is part of the Berkeley Student Cooperative.',
          'languageIcons': ['reactjs.svg', 'html.svg', 'css.svg', 'php.svg'],
          'thumbnail': {
            'filename': 'wasteSplash.jpg',
            'title': 'Casa Zimbabwe',
            'alt': 'The courtyard of Casa Zimbabwe'
          },
          'description': 'The unit houses 124 students and produces a massive amount of waste every year. As the former Waste Reduction Manager, I created this tool to have an accesible way of educating the residents on proper waste sorting practices as well as having an easy to manage educational resource for future WRM’s.',
          'technology': 'Both the user and admin clients are built in ReactJS and are fully responsive. The data is stored in a REST API written in PHP.',
          'features': [
              'User client with color coded panels representing each type of waste.',
              'Admin client for managing content. Panels can be created, deleted, edited, as well as reordered. Same goes for the content within each panel.',
              'Data stored in fully documented REST API.'
          ],
          'contributions': [
              'Drew initial sketches and final designs in Figma',
              'Built HTML templates based on designs',
              'Utilized ReactJS to build both the user and admin clients',
              'Designed and built the REST API from scratch in PHP',
              'Tested REST API using Postman',
              'Setup hosting for the site on the local server within the housing unit'
          ],
          'image1': {
            'filename': 'wasteUserDash.jpg',
            'title': 'User Dashboard',
            'alt': 'Screenshot of user dashboard'
          },
          'image2': {
            'filename': 'wasteAdminDash.jpg',
            'title': 'Admin Dashboard',
            'alt': 'Screenshot of adminitrator dashboard'
          },
          'links': [
            {'title': 'Go to website', 'link': 'https://cz-waste.herokuapp.com/'},
            {'title': 'Checkout the code', 'link': 'https://github.com/Roberto-Cardenas/cz-waste'}
          ]
        }
      ]
    }

    return projects[language]

  def getProjects(self):
    return self.projects

  def getProject(self, projectId):
    return self.projects[projectId]
    