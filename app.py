import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

# app.config["SQLALCHEMY_DATABASE_URI"] = " URL here"
# db = SQLAlchemy(app)

# Base = automap_base()
# Base.prepare(db.engine, reflect=True)

#create route that renders index.html
@app.route("/")
def home():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/api/categories")
def categories():
    
    return jsonify()

@app.route("/api/#extremeweather")
def extremeweather():

    return jsonify(data)

@app.route("/api/#severeweather")
def extremeweather():

    return jsonify(data)

if __name__ == "__main__":
    app.run()