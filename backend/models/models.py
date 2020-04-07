import requests
import pprint
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import json
import sys
from sqlalchemy import create_engine

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres://parth_shah:hello@localhost:5432/college"
db = SQLAlchemy(app)


db.create_all()
db.session.commit()

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])





