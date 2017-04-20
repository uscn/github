import webapp2
 
class ShowHome(webapp2.RequestHandler):
    def get(self):
application = webapp2.WSGIApplication([
    ('/', ShowHome),
], debug=True)
