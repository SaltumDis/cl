import json
import requests
import sys
from flask import Flask
from flask import render_template
from flask import request as req
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

api = ""
url = ""

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
        return render_template('result.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
