#login
import json
from getpass import getpass

def login():
	with open("data/dogers.json", "r") as u:
		dogers = json.load(u)
		name = input("Enter login:\t")
		password = getpass("Enter Password\t")

		if name in dogers.keys():
			if name == dogers[name]["name"] and password == dogers[name]["password"]:
				return name
			else:
				print("Sorry, try again")
		else:
			print("there is no doger with this name")