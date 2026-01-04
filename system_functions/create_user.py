#add doge
import json

BANNED_CHARACTERS = ["{" ,"}", "\\", "[", "]", "(", ")", "<", ">", "\'", "\"", "/" " "]
BANNED_WORDS = ["err", "error"]
def create_user():
	dogers = {}
	with open("data/dogers.json", "r") as d:
		dogers = json.load(d)
	
	name = input("Enter Name:\t")
	password = input("Enter Password:\t")
	if name.strip() and password.strip():
		if not name in dogers.keys():
			if len(dogers.keys()) == 1 and list(dogers.keys())[0] == "imperator":
				dogers["imperator"]["password"] = password

			for i in BANNED_CHARACTERS:
				if i in name:
					print(f"err: You cant use {i} character")
					break
				if i in password:
					print(f"err: You cant use {i} character")
					break
			else:
				for i in BANNED_WORDS:
					if i == name:
						print(f"err: You cant use \"{i}\" as your name")
						break
					if i == password:
						print(f"err: You cant use {i} as your password")
						break
				else:
					with open("data/dogers.json", "w") as d:
						dogers[name] = {"name" : name, "password" : password}
						json.dump(dogers, d)
						
		else:
			print("err: This name is already exist")
	else:
		print("err: Name or password should have at least one character")
