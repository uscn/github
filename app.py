import webapp2
 
class ShowHome(webapp2.RequestHandler):
    def get(self):
        temp_data = {}
        temp_path = 'index.html'
        self.response.out.write(template.render(temp_path,temp_data))
      
application = webapp2.WSGIApplication([
    ('/', ShowHome),
], debug=True)
