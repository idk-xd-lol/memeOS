#kernel
from functions import Functions
from shell import Shell
import json
from getpass import getpass

class Kernel:
	def __init__(self):
		"""System start"""
		self.functions = Functions()
		self.tries = 0 #password guess tries
		self.name = self.login()

		while self.name == "error":
			self.name = self.login()

			if self.tries == 5:
				quit()

		self.shell = Shell(self.name, self.functions)
		self.shell.run()

	def login(self):
		"""Logining"""
		with open("data/users.json", "r") as u:
			dogers = json.load(u)
			name = input("Enter login:\t")
			password = getpass("Enter Password:\t")

			if name in dogers.keys():
				if name == dogers[name]["name"] and password == dogers[name]["password"]:
					return dogers[name]["name"]

				else:
					print("Sorry, try again")
					self.tries += 1
					return "error"
			else:
				print("there is no user with this name, try again")
				return "error"
k = Kernel()