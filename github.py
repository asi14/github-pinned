import requests
import getpass
import json
import datetime

url = 'https://api.github.com/user/repos'
url_4 = 'https://api.github.com/graphql'

def pull_v3(username,password):#lists full repo, NOT pinned repos, also needs to handle bad passwords
	#creates today's date and margin to test for repos actively maintained
	today = datetime.datetime.today()
	margin = datetime.timedelta(days=30)

	#sends request to github and converts to json
	r = requests.get(url, auth=(username,password))
	json_stuff = r.json()

	#gets commit's last commit and sees if falls in margin
	for i in json_stuff:
		#gets datetime object of last commmit
		datetime_object = datetime.datetime.strptime(i['pushed_at'],"%Y-%m-%dT%H:%M:%SZ")

		#margin comparison
		if(today-datetime_object<margin):
			print(i['name'])
			r_lang = requests.get('https://api.github.com/repos/%s/%s/languages' %(username,i['name'])).json()
			print(r_lang)
def pull_v4(): #need to resolve oauth problems
	r = requets.get('https://github.com/login/oauth/authorize')
	print(json.dumps(r.json(), indent=4, sort_keys=True))
#user enters password manually, such that password isn't stored
def user_enter():
	username = input("Enter username: ")
	password = getpass.getpass("Enter password: ")
	pull_v3(username,password)
user_enter()
