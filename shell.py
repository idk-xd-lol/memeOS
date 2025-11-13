#shell
class Shell:
	def __init__(self, user, functions):
		self.user = user
		self.funcs = functions
		self.isrun = True

	def run(self):
		while self.isrun:
			cmd = input(f"{self.user}@meme>")
			cmd_list = self.kernel.commands
			if cmd in kernel_cmds:
				self.kernel.get_command(command)
			elif command == "exit":
				self.isrun = False
			else:
				print(f"err: Command '{cmd}' not found")

