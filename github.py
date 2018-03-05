import requests
import getpass
import json
import datetime

url = 'https://api.github.com/user/repos'
url_4 = 'https://api.github.com/graphql'

def pull_v3(username,password):#lists full repo, NOT pinned repos, also needs to handle bad passwords
	today = datetime.datetime.today()
	margin = datetime.timedelta(days=30)
	r = requests.get(url, auth=(username,password))
	#print(r.url)
	#print(json.dumps(r.json(), indent=4, sort_keys=True))
	json_stuff = r.json()
	for i in json_stuff:
		datetime_object = datetime.datetime.strptime(i['pushed_at'],"%Y-%m-%dT%H:%M:%SZ")
		if(today-datetime_object<margin):
			print(i['name'])
			print(i['language'])
			print(datetime_object)
def pull_v4(): #need to resolve oauth problems
	r = requets.get('https://github.com/login/oauth/authorize')
	print(json.dumps(r.json(), indent=4, sort_keys=True))
def user_enter():
	username = input("Enter username: ")
	password = getpass.getpass("Enter password: ")
	pull_v3(username,password)
user_enter()
