#application
import json
class App:
	def __init__(self):
		self.apps = {}
		self.__get_apps()

	def __get_apps(self):
		try:
			with open ("data/apps.json", "r") as a:
				self.apps = json.load(a)
		except:
			with open ("data/apps.json", "w") as w:
				json.dump({}, w)
			print("There are no applications there, try to 'imp app app-name' or add application from package")
			
	def open_python_app(self, app_name):
		path = self.apps[app_name]
	    
		with open(path) as f:
			code = f.read()

		env = {"__builtins__": __builtins__}
		exec(code, env)
		env[app_name]()

	def app_manager(self, app_name):
		path = self.apps[app_name]
	    
		if ".py" in path:
			self.open_python_app(app_name)

def app(name):
	a = App()
	a.app_manager(name)