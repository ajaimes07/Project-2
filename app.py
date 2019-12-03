from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
import pymongo
import sys
import json


app = Flask(__name__)
# conn = 'mongodb://localhost:27017/project2rice_app'
# client = pymongo.MongoClient(conn)
# app.config['MONGO_DBNAME'] = 'project2rice'
app.config['MONGO_URI'] = 'mongodb://project2:project2@ds121262.mlab.com:21262/heroku_8r6fdxgl'
mongo = PyMongo(app)
# connect to mongo db and collection
# db = client.heroku_8r6fdxgl

@app.route("/")
def Home():
    """Return the homepage."""
    return render_template("index.html")

@app.route('/severe')
def severe():
    return render_template('severe.html')

@app.route('/fire')
def fire():
    return render_template('fire.html')

@app.route('/flood')
def flood():
    return render_template('flood.html')

@app.route('/leaflet')
def flood():
    return render_template('leaflet.html')

@app.route("/#Fires", methods=['GET'])
def get_all_fires():
    fires = mongo.db.fires
    output = []
    for f in fires.find() :
        output.append({'location': f['location'], 'date' : f['date']})
    return jsonify({'result' : output})



@app.route("/#Floods", methods=['GET'])
def get_all_floods():
    floods = mongo.db.floods
    output = []
    for F in floods.find() :
        output.append({'location': F['location'], 'date' : F['date']})
    return jsonify({'result' : output})



@app.route("/#SevereWeather", methods=['GET'])
def get_all_severeweather():
    severeweather = mongo.db.severeweather
    output = []
    for s in severeweather.find() :
        output.append({'location': s['location'], 'date' : s['date']})
    return jsonify({'result' : output})


# with open('fire.json','w') as f:
#     json.dump(request.form, f)
#     return render_html('flood.html')

if __name__ == "__main__":
    app.run(debug=True)