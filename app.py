import requests
from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
import pymongo
import sys


app = Flask(__name__)

# conn = 'mongodb://localhost:27017/project2rice_app'
# client = pymongo.MongoClient(conn)

app.config['MONGO_DBNAME'] = 'project2rice'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/project2rice'

mongo = PyMongo(app)
# connect to mongo db and collection
# db = client.heroku_8r6fdxgl
# collection = db.floods
# collection = db.fires

#create route that renders index.html
@app.route("/")
def Home():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/fire", methods=['GET'])
def get_all_fires():
    fires = mongo.db.fires
    output = []
    for f in fires.find() :
        output.append({'location': f['location'], 'date' : f['$date']})
    return jsonify({'result' : output})

@app.route("/flood")
def flood():
    # write a statement that finds all the items in the db and sets it to a variable 
    floods = list(db.collection.find())
    print(floods)
    return render_template("flood.html",floods=floods)

if __name__ == "__main__":
    app.run(debug=True)