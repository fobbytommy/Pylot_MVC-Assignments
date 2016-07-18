from system.core.controller import *
from time import localtime, strftime

class TimeDisplay(Controller):
	def __init__(self, action):
		super(TimeDisplay, self).__init__(action)
		self.load_model('WelcomeModel')
		self.db = self._app.db
	def index(self):
		current_time = strftime("%b %d, %Y %I:%M %p", localtime())
		return self.load_view('index.html', time = current_time)
