import json
import requests
from flask import current_app, render_template, make_response
from . import main


@main.route('/', methods=['GET'])
def index():
    response = make_response(render_template('views/index.html'))
    return response


@main.route('/cases', methods=['GET'])
def cases():
    apiURL = "http://192.168.4.230:8000/api/v1/tasks/"
    getData = requests.get(apiURL)

    if getData.status_code == 200:
        jsonData = getData.json()
    else:
        print(f"Error retrieving data, {getData.status_code}")
    
    data = json.dumps(jsonData)
    cases = json.loads(data)

    response = make_response(render_template('views/cases.html', cases = cases))

    return response