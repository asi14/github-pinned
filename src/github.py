import requests
import getpass
import json
import datetime

#make compiling of output json an independent method
#begin latex integration
#add comments (again)
#optional args

url = 'https://api.github.com/user/repos'
url_4 = 'https://api.github.com/graphql'

def user_enter():
	username = input("Enter username: ")
	password = getpass.getpass("Enter password: ")
	r = requests.get(url, auth=(username,password), params = {'sort':'pushed'})
	json_stuff = r.json()
	return [json_stuff,username]
	
def pull_margin(number_days):#gets repos with latest updates from within a month
	
	user_enter_output = user_enter()
	request_json =  user_enter_output[0]
	username = user_enter_output[1]

	today = datetime.datetime.today()
	margin = datetime.timedelta(days=number_days)

	data_output = {}

	for i in request_json:
		datetime_object = datetime.datetime.strptime(i['pushed_at'],"%Y-%m-%dT%H:%M:%SZ")

		if(today-datetime_object<margin):
			r_lang = requests.get('https://api.github.com/repos/%s/%s/languages' %(username,i['name'])).json()
			data_output[i['name']] = {'languages':r_lang,'description':i['description']}
	data_json = json.dumps(data_output, indent=4, sort_keys=True)
	return data_json		
def pull_last_number(number_repos): #pulls the latest n repos
	user_enter_output = user_enter()
	request_json = user_enter_output[0]
	username = user_enter_output[1]

	data_output = {}

	for i in range(number_repos):
		r_lang = requests.get('https://api.github.com/repos/%s/%s/languages' %(username,request_json[i]['name'])).json()
		data_output[request_json[i]['name']] = {'languages':r_lang,'description':request_json[i]['description']}
	data_json = json.dumps(data_output, indent=4, sort_keys=True)
	return data_json		
def pull_v4(): #need to resolve oauth problems
	r = requets.get('https://github.com/login/oauth/authorize')
	print(json.dumps(r.json(), indent=4, sort_keys=True))
if __name__ == '__main__':
	print(pull_last_number(3))
