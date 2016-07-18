from system.core.controller import *
class Surveys(Controller):
	def __init__(self, action):
		super(Surveys, self).__init__(action)
	def index(self):
		return self.load_view('index.html')
	def process(self):
		session['name'] = request.form['name']
		session['location'] = request.form['location']
		session['language'] = request.form['language']
		session['comment'] = request.form['comment']
		errors = []
		if len(session['name']) < 1:
			errors.append('Please put your name!')
		elif str.isalpha(str(session['name'])) == False:
			errors.append('NO symbols or numbers for your name!')
		if errors:
			for error in errors:
				flash(error)
			return redirect('/')
		else:
			return redirect('/result')

	def result(self):
		try:
			session['count'] += 1
		except:
			session['count'] = 1
		return self.load_view('result.html')
