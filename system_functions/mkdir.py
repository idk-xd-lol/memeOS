import os

def mkdir(path = None):
	if path == None:
		path = input("Enter memes name or path:")
	if path.strip():
		os.makedirs(path)
	else:
		print("err: You couldn't create a memes with empty name")