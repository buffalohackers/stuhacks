import json
import os

import flask
import requests

app = flask.Flask(__name__)

@app.route("/")
def index():
	resp = dict()
	hackathons = [0]
	p = {'limit': 100, 'offset': 0}
	while hackathons:
		r = requests.get('https://www.hackerleague.org/api/v1/hackathons.json', params=p)
		hackathons = r.json()
		for hackathon in hackathons:
			if hackathon['students_only']:
				resp[hackathon['id']] = hackathon['name']
		p['offset'] += 1
	return '<br/>'.join(resp.values())

if __name__ == "__main__":
	app.run()
