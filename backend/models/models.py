import requests
import pprint
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import json
import sys
from sqlalchemy import create_engine

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres://pshah:hello@localhost:5432/chaosmonkey"
db = SQLAlchemy(app)

class Logs(db.Model):
    __tablename__ = "Logs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(), nullable=False, unique=False)
    text = db.Column(db.String(), nullable=False, unique=False)
    container = db.Column(db.String(), nullable=False, unique=False)

class Jobs(db.Model):
    __tablename__ = "Jobs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_time = db.Column(db.String(), nullable=False, unique=False)
    end_time = db.Column(db.String(), nullable=False, unique=True)
    stress_test = db.Column(db.String(), nullable=False, unique=False)


db.create_all()
db.session.commit()

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])





