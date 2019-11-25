# Dependencies
import pymongo
import datetime
import pandas as pd

# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Declare the database
db = client.Project2

# Declare the collection
#collection = db#.fruits_db
collection = db.NEON_db

dfItems = pd.read_csv('NEON_field-sites.csv')
columns = dfItems.columns
colList = []
for index, row in dfItems.iterrows():
    for c in columns:
        cc = '{}:{}'.format(c,row[c])
        colList.append(cc)

    #post = {colList}  # Converting list to dictionary
    post = colList  # Converting list to dictionary
# Insert the document into the database
    collection.insert_one(post)    
#    post = {
    #     'sitename': row['Site Name'],
    #     'siteid': row['Site ID']}
    # collection.insert_one(post)    

# Verify results:
#results = db.fruits_db.find()
results = db.NEON.find()
for result in results:
    print(result)
