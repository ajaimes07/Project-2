import os
import pandas as pd
import numpy as np
import requests
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
import pymongo



app = Flask(__name__)


#################################################
# Database Setup
#################################################

# app.config["SQLALCHEMY_DATABASE_URI"] = " URL here"
# db = SQLAlchemy(app)
# mongo = PyMongo(app, uri="mongodb://localhost:27017/project2rice_app")
conn = 'mongodb://localhost:27017/project2rice_app'
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.heroku_8r6fdxgl
collection = db.Droughts
collection = db.floods
collection = db.fires



# Base = automap_base()
# Base.prepare(db.engine, reflect=True)

#create route that renders index.html
@app.route("/")
def Home():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/geomap")
def geomap():
    
    return render_template("comparison.html")

@app.route("/categories")
def categories():

    return render_template("photos2.html")

# @app.route("/data")
# def data():

#     return jsonify("data.html")

if __name__ == "__main__":
    app.run()