from flask import current_app, render_template, make_response
from . import main


@main.route('/', methods=['GET'])
def index():
    response = make_response(render_template('views/index.html'))
    return response