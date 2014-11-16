import webapp2

form="""
<form method="post">
	<input name="q">
	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(form)

	def post(self):
		self.response.out.write("dummy")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
