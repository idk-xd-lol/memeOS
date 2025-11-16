#dogelist
import json

def dogelist():
	with open("data/dogers.json", "r") as u:
		doges = json.load(u)
		for i in doges:
			print(doges.get(i)['name'])