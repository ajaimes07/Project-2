import os
import pandas as pd
import numpy as np
import requests
from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
import pymongo

app = Flask(__name__)

#################################################
# Database Setup
#################################################

# mongo = PyMongo(app, uri="mongodb://localhost:27017/project2rice_app")
conn = 'mongodb://localhost:27017/project2rice_app'
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.heroku_8r6fdxgl
collection = db.Droughts
collection = db.floods
collection = db.fires

#create route that renders index.html
@app.route("/")
def Home():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/wildfire")
def wildfire():
    
    return render_template("wildfire.html")

@app.route("/hurricane")
def hurricane():

    return render_template("hurricane.html")

@app.route("/flood")
def flood():

    return render_template("flood.html")
 # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run()