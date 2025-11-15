#cmd defs
import json

class Functions:

	def __init__(self):
		self.functions = {}
		self.__get_def()

	def __get_def(self):
		try:
			with open ("data/functions.json", "r") as o:
				self.functions = json.load(o)
		except:
			raise "You maybe have delete this file, try to reinstall system"

	def exec_cmd(self, name, *args):
	    with open("data/functions.json") as r:
	        functions = json.load(r)
	        path = functions[name]
	    
	    with open(path) as f:
	        code = f.read()

	    env = {"__builtins__": __builtins__}
	    exec(code, env)
	    env[name](*args)
