import calendar
import datetime
import json
import os

import flask
import requests

app = flask.Flask(__name__)

@app.route('/')
def index():
    resp_hackathons = list()
    complete = False
    p = {'limit': 100, 'offset': 0}
    while not complete:
        r = requests.get('https://www.hackerleague.org/api/v1/hackathons.json', params=p)
        hackathons = r.json()
        for hackathon in hackathons:
            if hackathon['students_only'] and hackathon['state'] != 'complete':
                resp_hackathons.append(hackathon)
            elif hackathon['state'] == 'complete':
                complete = True
                break
        p['offset'] += 1
    resp_hackathons = sorted(resp_hackathons, key=lambda x: x['start_time'])
    return flask.render_template('index.html', hackathons=resp_hackathons)

@app.route('/about')
def about():
    return flask.render_template('about.html')

if __name__ == "__main__":
    app.run()
