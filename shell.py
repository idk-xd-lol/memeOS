#shell
import json
from functions import Functions

class Shell:
	def __init__(self, user, functions):
		self.user = user
		self.funcs = functions
		self.isrun = True

	def run(self, *args):
		while self.isrun:
			cmd_list = self.__get_def().keys()
			raw = input(f"{self.user}@meme>")
			if not raw.strip():
				continue
			parts = raw.split()
			cmd = parts[0]
			args = parts[1:]

			if cmd in cmd_list:
				try:
					self.funcs.exec_cmd(cmd, *args)
				except Exception as e:
					print("err:", e)
			elif cmd == "exit":
				self.isrun = False
			else:
				print(f"err: Command '{cmd}' not found")

	def __get_def(self):
		try:
			with open ("data/functions.json", "r") as o:
				return json.load(o)
		except:
			raise "You maybe have delete this file, try to reinstall system"

f = Functions()
sh = Shell("nobody", f)
sh.run()