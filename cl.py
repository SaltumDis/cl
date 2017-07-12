import json
import os

import requests
import sys
from flask import Flask
from flask import render_template
from flask import request as req
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

api = "f4a8cc506a606f627c3aea89886a3ae4-us13"
url = "https://us13.api.mailchimp.com/3.0/lists/34b4669e4c/members/"
filename = os.path.join(os.path.dirname(sys.argv[0]),'urls.txt')


@app.route('/', methods=['GET', 'POST'])
def index():
    if req.method == 'POST':
        user = req.form.get("user")
        email = req.form.get("email")
        dict = {
            "email_address": email,
            "status": "subscribed",
            "merge_fields": {
                "FNAME": user

            }}
        requests.post(url, data=json.dumps(dict), auth=HTTPBasicAuth('user', api))
        lines = [line.rstrip('\n') for line in open(filename)]
        return render_template('edit.html', urls=lines)
    return render_template('index.html')

@app.route('/test')
def test():
    lines = [line.rstrip('\n') for line in open(filename)]
    return render_template('edit.html', urls=lines)

@app.route('/links', methods=['POST', 'GET'])
def do_admin_login():
    if req.method == 'POST':
        if req.form['key'] == 'james':
            links=req.form['links']
            with open(filename, 'w') as file:
                file.write(links)
            return render_template('login.html', changed=True, links=links)
    with open(filename, 'r') as myfile:
        data = myfile.read()
    return render_template('login.html',links=data)


if __name__ == '__main__':
    app.run()
