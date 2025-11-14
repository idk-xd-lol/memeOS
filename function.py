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

	def exec_func(self, name, *args):
		with open("data/functions.json") as r:
			code = json.load(r)
			code = code[name]
			print(code)
		env = {}
		exec(code, env)
		env[name](*args)