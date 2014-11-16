import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('Hello, webapp world!')

app = webapp2.WSGIApplication([('/', MainHandler)], 
								debug=True)
