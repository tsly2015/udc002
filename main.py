import webapp2

form="""
<form action="http://www.google.com/search">
	<input name="q">
	<input type="submit">
</form>
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
		#self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(form)

app = webapp2.WSGIApplication([('/', MainHandler)], 
								debug=True)
