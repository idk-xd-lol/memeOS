#dev dogelist
#doge list for load with
import json

def dev_dogelist():
	with open("data/dogers.json", "r") as u:
		c = json.load(u)
		return c