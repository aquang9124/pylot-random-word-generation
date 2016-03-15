from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
	def index(self):
		return self.load_view('index.html')
	def test(self):
		apples = "jimmy"
		return "This is a test for custom rules and redirect"
	def magic(self):
		return redirect('/awesome')
	def process(self):
		print request.form['name']
		return redirect('/')
		