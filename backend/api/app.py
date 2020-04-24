from flask import Flask
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
import json
import requests
from sqlalchemy import create_engine, or_, func, desc
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS
from flask import request
from flask import Response
from sqlalchemy import inspect

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "{Chaos API}"

@app.route('/chaos/regex')
def add_regular_expression():
    return "add regular expression"

@app.route('/chaos/regex/all')
def all_regular_expressions():
    return "all regular expressions"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


