import webapp2
from google.appengine.ext.webapp import template
import os

class MainPage(webapp2.RequestHandler):
    def get(self):
        # Path to the template folder
        path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
        self.response.write(template.render(path, {}))  # Render the template

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
