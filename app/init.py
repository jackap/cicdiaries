from flask import Flask
import requests
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_public_repos():	
	'''
	r = requests.get("https://api.github.com/users/jackap/repos")
	repos = list()
	json_request = json.loads(r.content)
	print(r.content)
	for repo in json_request:
		if 'name' in repo:
			repos.append({'name': repo['name'],
				'description': repo['description'],
				'html_url': repo['html_url'],
				'date' : repo['created_at'],
				})
	'''
	return json.dumps({"data": [{"name": "CobraKing", "description": "A more secure color barcode streaming for smartphone systems", "html_url": "https://github.com/jackap/CobraKing", "date": "2017-11-15T13:31:39Z"}, {"name": "forking-workflow-exercise", "description": "Exercise to practice collaborative forking workflow.", "html_url": "https://github.com/jackap/forking-workflow-exercise", "date": "2018-05-30T07:41:08Z"}, {"name": "git-rebase-squash-exercise", "description": "Git rebase and commit squashing exercise.", "html_url": "https://github.com/jackap/git-rebase-squash-exercise", "date": "2018-05-30T09:54:06Z"}, {"name": "Hacking-password", "description": "Simple program to make a dictionary attack on a database", "html_url": "https://github.com/jackap/Hacking-password", "date": "2017-01-13T16:09:02Z"}, {"name": "ide-examples", "description": "Examples to demonstrate the usage of IDE.", "html_url": "https://github.com/jackap/ide-examples", "date": "2018-05-30T11:11:47Z"}, {"name": "Ketje", "description": "Implementation of Ketje cryptographic function", "html_url": "https://github.com/jackap/Ketje", "date": "2017-01-13T16:00:49Z"}, {"name": "Mobile-Cloud-Computing-Dockers", "description": "Second project of the course Mobile Cloud Computing of the Aalto University", "html_url": "https://github.com/jackap/Mobile-Cloud-Computing-Dockers", "date": "2017-01-13T15:41:57Z"}, {"name": "Mobile-Cloud-Computing-VNC", "description": "First project of the course Mobile Cloud Computing of the Aalto University", "html_url": "https://github.com/jackap/Mobile-Cloud-Computing-VNC", "date": "2017-01-13T16:35:06Z"}, {"name": "SHA3-256", "description": "Implementation of the SHA3-256 algorithm", "html_url": "https://github.com/jackap/SHA3-256", "date": "2017-01-13T15:55:05Z"}, {"name": "VRTPW", "description": "Project for the course Optimization Methods and Algorithms at Politecnico di Torino", "html_url": "https://github.com/jackap/VRTPW", "date": "2017-01-13T16:45:01Z"}]})

@app.route('/code')
def hello_world():
	return get_public_repos()
   

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=8080)
