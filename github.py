import requests
import json
url = 'https://api.github.com/user/repos'

def pull(username,password):
	r = requests.get(url, auth=(username,password))
	#print(r.url)
	#print(json.dumps(r.json(), indent=4, sort_keys=True))
	json_stuff = r.json()
	for i in json_stuff:
		print(i['name'])
		print(i['language'])
