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
          'description': 'The unit houses 124 students and produces a massive amount of waste every semester. As the former Waste Reduction Manager, I created this tool to have an accessible way of educating the residents on proper waste sorting practices as well as having an easy to manage educational resource for future WRM’s.',
          'technology': 'Both the user and admin clients are built in ReactJS and are fully responsive. The data is stored in a REST API written in PHP.',
          'features': [
              'User client with color coded panels representing each type of waste.',
              'Admin client for managing content. Panels can be created, deleted, edited, as well as reordered. Same goes for the content within each panel.',
              'Data stored in fully documented REST API.'
          ],
          'contributions': [
              'Drew initial sketches and final designs in Figma.',
              'Built HTML templates based on designs.',
              'Utilized ReactJS to build both the user and admin clients.',
              'Designed and built the REST API from scratch in PHP.',
              'Tested REST API using Postman.',
              'Setup hosting for the site on the local server within the housing unit.'
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
            {'title': 'Github', 'link': 'https://github.com/Roberto-Cardenas/cz-waste'}
          ]
        },
        {
          'title': 'CZ Weekly Menu Website',
          'shortDescription': 'Weekly Menu Website for Casa Zimbabwe, a student housing unit that is part of the Berkeley Student Cooperative.',
          'languageIcons': ['html.svg', 'css.svg'],
          'thumbnail': {
            'filename': 'menuWeeklyMenu.jpg',
            'title': 'Weekly Menu',
            'alt': 'CZ Weekly Menu'
          },
          'description': 'The house provides access to groceries, an industrial kitchen, and daily hot meals to all of its 124 residents. As the person in charge of managing all of these food related logistics, I created this website as a tool to keep residents updated on what they will be eating each day, as well as providing them relevant food information and announcements for the week.',
          'technology': 'This fully responsive website was designed in Figma and built using HTML and Sass.',
          'features': [
              'I took inspiration from looking at how restaurants display their menus on their websites.',
              'The menu resizes with the screen but never changes its internal layout, instead behaving very similarly to a pdf.'
          ],
          'contributions': [
              'Drew initial sketches and final designs in Figma.',
              'Utilized HTML and Sass to build the website.'
          ],
          'image1': {
            'filename': 'menuWeeklyMenu.jpg',
            'title': 'Full Design',
            'alt': 'CZ Weekly Menu'
          },
          'links': [
            {'title': 'Go to website', 'link': 'https://roberto-cardenas.github.io/cz-dinner-menu/'},
            {'title': 'Github', 'link': 'https://github.com/Roberto-Cardenas/cz-dinner-menu/'},
            {'title': 'Figma', 'link': 'https://www.figma.com/file/A2SsFKPMGCMNME3D2i64DN/CZ-Dinner-Menu?node-id=0%3A1&t=KjcppbUuHHQf1tXP-1'}
          ]
        },
        {
          'title': 'Izzy Davies Design',
          'shortDescription': 'Design Portfolio for Izzy Davies, a Bristol born graphic designer with a passion for using color, composition, and 3d work to create beautiful narrative-led designs.',
          'languageIcons': ['html.svg', 'css.svg'],
          'thumbnail': {
            'filename': 'izzyDaviesDesignSplash.jpg',
            'title': 'Home Page',
            'alt': 'Home Page'
          },
          'description': 'Because of the nature of Izzy’s work, it was imperative to choose a layout design that did not take away from her stunning graphics and instead used them to create a visually appealing portfolio.',
          'technology': 'This fully responsive website was designed in Figma and built using HTML and Sass.',
          'features': [
              'This website features an index of projects showcased in a masonry layout, a page for each individual project and an about page.'
          ],
          'contributions': [
              'Slightly redesigned the original Cargo template and prototyped it in Figma.',
              'Utilized HTML and Sass to build the website.'
          ],
          'image1': {
            'filename': 'izzyDaviesDesignProjectPage.jpg',
            'title': 'Project Page',
            'alt': 'Project Page'
          },
          'links': [
            {'title': 'Go to website', 'link': 'https://roberto-cardenas.github.io/izzydaviesportfolio/'},
            {'title': 'Github', 'link': 'https://github.com/Roberto-Cardenas/izzydaviesportfolio/'},
            {'title': 'Figma', 'link': 'https://www.figma.com/file/gks7s0owA7qdLwU5XxeGkQ/Izzy-Davies-Design?node-id=0%3A1&t=DRcPKf1myuq8ARV2-1'}
          ]
        }
      ]
    }

    return projects[language]

  def getProjects(self):
    return self.projects

  def getProject(self, projectId):
    return self.projects[projectId]
    