import calendar
import datetime
import json
import os

import flask
import requests

app = flask.Flask(__name__)

@app.route("/")
def index():
	resp_hackathons = list()
	hackathons = [0]
	p = {'limit': 100, 'offset': 0}
	while hackathons:
		r = requests.get('https://www.hackerleague.org/api/v1/hackathons.json', params=p)
		hackathons = r.json()
		for hackathon in hackathons:
			if hackathon['students_only'] and hackathon['state'] != 'complete':
				resp_hackathons.append(hackathon)
		p['offset'] += 1
	resp_hackathons.reverse()
	return flask.render_template('index.html', hackathons=resp_hackathons)

if __name__ == "__main__":
	app.run()
