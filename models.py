class Projects():
  def __init__(self, language):
    self.projects = self.loadProjects(language)

  def loadProjects(self, language):
    projects = {
      'en': [
        {
          'title': 'CZ Waste Website',
          'shortDescription': 'Waste Information Website for Casa Zimbabwe, a student housing unit that is part of the Berkeley Student Cooperative.',
          'description': 'The intention of this website is to allow the Waste Reduction Manager of the unit to provide an accesible and centralized way for members of the cooperative to find the relevant information when it comes to sorting waste properly in the 124 person unit. The WRM can easily update this information by using the companion administrator page.',
          'description2': 'The client is built utilizing ReactJS and is fully responsive. The website consumes its data from a simple API written in PHP.',
          'languageIcons': ['reactjs.svg', 'html.svg', 'css.svg'],
          'thumbnail': 'goToSiteBtn.jpg',
          'github': 'https://github.com/Roberto-Cardenas/cz-waste',
          'website': 'https://cz-waste.herokuapp.com/'
        },
        {
          'title': 'CZ Waste Website Admin',
          'shortDescription': 'Administrator website for the Casa Zimbabwe Waste Information Website. Casa Zimbabwe is a student housing unit that is part of the Berkeley Student Cooperative.',
          'description': 'The intention of this website is to allow the Waste Reduction Manager of the unit to provide an accesible and centralized way for members of the cooperative to find the relevant information when it comes to sorting waste properly in the 124 person unit.',
          'description2': 'The client is built utilizing ReactJS and is fully responsive. The website consumes and writes its data from and to a simple API written in PHP. ',
          'languageIcons': ['reactjs.svg', 'html.svg', 'css.svg'],
          'thumbnail': 'goToSiteBtn.jpg',
          'github': 'https://github.com/Roberto-Cardenas/cz-waste-admin',
          'website': 'https://cz-waste-admin.herokuapp.com/'
        },
        {
          'title': 'CZ Waste REST API',
          'shortDescription': 'REST API for the Casa Zimbabwe Waste Information Website and its companion Administrator tool. Casa Zimbabwe is a student housing unit that is part of the Berkeley Student Cooperative.',
          'description': 'Simple REST API that serves as the backend for both the Casa Zimbabwe Waste Website and its companion Administrator page. Documentation on the API can be found by following the Github link.',
          'description2': 'The API itself is written in PHP and the data is stored in JSON files.',
          'languageIcons': ['php.svg'],
          'thumbnail': 'goToSiteBtn.jpg',
          'github': 'https://github.com/Roberto-Cardenas/cz-waste-api',
          'website': 'https://cz-waste-api.herokuapp.com/'
        }
      ]
    }

    return projects[language]

  def getProjects(self):
    return self.projects

  def getProject(self, projectId):
    return self.projects[projectId]
    