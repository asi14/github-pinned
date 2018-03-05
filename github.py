import requests
import json
url = 'https://api.github.com/user/repos'
url_4 = 'https://api.github.com/graphql'

def pull_v3(username,password):#lists full repo, NOT pinned repos
	r = requests.get(url, auth=(username,password))
	#print(r.url)
	#print(json.dumps(r.json(), indent=4, sort_keys=True))
	json_stuff = r.json()
	for i in json_stuff:
		print(i['name'])
		print(i['language'])
		print(i['updated_at'])
def pull_v4(): #need to resolve oauth problems
	r = requets.get('https://github.com/login/oauth/authorize')
	print(json.dumps(r.json(), indent=4, sort_keys=True))
def user_enter():
	username = input("Enter username: ")
	password = input("Enter password: ")
	pull_v3(username,password)
user_enter()
