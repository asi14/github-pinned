import requests
import getpass
import json
import datetime

url = 'https://api.github.com/user/repos'
url_4 = 'https://api.github.com/graphql'

def pull_v3(username,password):#gets repos with latest updates from within a month
	#creates today's date and margin to test for repos actively maintained
	today = datetime.datetime.today()
	margin = datetime.timedelta(days=30)

	#sends request to github and converts to json
	r = requests.get(url, auth=(username,password))
	json_stuff = r.json()

	data_output = {}

	#gets commit's last commit and sees if falls in margin
	for i in json_stuff:
		#gets datetime object of last commmit
		datetime_object = datetime.datetime.strptime(i['pushed_at'],"%Y-%m-%dT%H:%M:%SZ")

		#margin comparison
		if(today-datetime_object<margin):
			r_lang = requests.get('https://api.github.com/repos/%s/%s/languages' %(username,i['name'])).json()
			data_output[i['name']] = {'languages':r_lang,'description':i['description']}
	data_json = json.dumps(data_output, indent=4, sort_keys=True)
	print(data_json)		
def pull_v4(): #need to resolve oauth problems
	r = requets.get('https://github.com/login/oauth/authorize')
	print(json.dumps(r.json(), indent=4, sort_keys=True))
#user enters password manually, such that password isn't stored
def user_enter():
	username = input("Enter username: ")
	password = getpass.getpass("Enter password: ")
	pull_v3(username,password)
if __name__ == '__main__':
	user_enter()
