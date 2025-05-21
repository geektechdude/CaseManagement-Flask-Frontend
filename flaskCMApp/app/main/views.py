import json
import requests
from flask import current_app, render_template, make_response
from . import main
from app import getData


@main.route('/', methods=['GET'])
def index():
    response = make_response(render_template('views/index.html'))
    return response


@main.route('/cases', methods=['GET'])
def cases():
    apiURL = "http://localhost:8000/api/v1/tasks/"
    cases = getData.get_data(apiURL)
    response = make_response(render_template('views/cases.html', cases = cases))
    return response

@main.route('/case/<int:id>', methods=['GET'])
def case(id):
    id = str(id)
    apiURL = "http://localhost:8000/api/v1/task/"+id
    case = getData.get_data(apiURL)
    response = make_response(render_template('views/case.html', case = case))
    return response