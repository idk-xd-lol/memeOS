#cmd defs
import json

class Functions:

	def __init__(self):
		self.functions = {}
		self.get_def()

	def get_def(self):
		try:
			with open ("data/functions.json", "r") as o:
				self.functions = json.load(o)
		except:
			raise "You maybe have delete this file, try to reinstall system"
				

f = Functions()