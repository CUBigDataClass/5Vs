import pymongo
import json
import datetime
import calendar

 # create an instance of the Mongodb client with a connection to our database on Mongolab.
client = pymongo.MongoClient("ds019980.mlab.com",19980)

# create a database called worldemotion
db=client['worldemotion']

#access the collection
collection=db['countryEmotion']

# MongoLab has user authentication
db.authenticate("5Vs", "bigdata2016")
times = collection.find()




timestamps = []
collections = []

for time in times:
    try:
        timestamp = time['country_emotion'][0]['current_time']
        print timestamp
        day_of_week = (timestamp[0:4])
        month_abbr = timestamp[4:7]
        month = list(calendar.month_abbr).index(month_abbr)
        day = int(timestamp[7:10])
        hour = int(timestamp[11:13])
        minute = int(timestamp[14:16])
        second = int(timestamp[17:19])
        year = int(timestamp[20:25])

        timestamps.append(datetime.datetime(year, month, day, hour, minute, second))
        collections.append(time['country_emotion'])
    except:
        pass


if (timestamps != []):
    most_recent = timestamps.index(max(timestamps))
    print collections[most_recent]
    print most_recent

    print collections


