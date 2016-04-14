import pymongo
import json

 # create an instance of the Mongodb client with a connection to our database on Mongolab.
client = pymongo.MongoClient("ds019980.mlab.com",19980)

# create a database called worldemotion
db=client['worldemotion']

#access the collection
collection=db['emotions']

# MongoLab has user authentication
db.authenticate("5Vs", "bigdata2016")
p = collection.find()


locations = {}
for tweet in p:
    locations.update({tweet['location_name']:tweet['tweet_emotion']})

for l in locations:
    print l, locations[l]


