from system.core.controller import *
import string
import random
class RandomGenerator(Controller):
	def __init__(self, action):
		super(RandomGenerator, self).__init__(action)
	def index(self):
		try:
			if session['attempt']:
				pass
		# if I get some error, that means session['attempt'] does not exist.
		# then inialize session['attempt'] equal to number one.
		except:
			session['attempt'] = 1
		session['random_word'] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(14))
		return self.load_view('index.html')
	def process(self):
		session['attempt'] += 1
		return redirect('/')
	def reset(self):
		session.pop('attempt')
		session.pop('random_word')
		return redirect('/')
