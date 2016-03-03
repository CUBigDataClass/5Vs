import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# Consumer keys and access tokens, used for OAuth
consumer_key = '***'
consumer_secret = '***'
access_token = '***'
access_secret = '***'

class Listener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('TweetsByLocation.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print "Error on_data: %s" % str(e)
        return True # To continue listening
 
    def on_error(self, status):
        print status
        return True # To continue listening

    def on_timeout(self):
        print 'Timeout...'
        return True # To continue listening
 
# OAuth process, using the keys and tokens
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Twitter Streaming
twitter_stream = Stream(auth, Listener())

# Bounding boxes to Retrieve tweets aroundthe following cities in the same order: New York City, London, Los Angeles, Chicago, Dallas, Philadelphia, 
# Manchester, Houston, Washington D.C., Toronto, Boston, San Francisco, Atlanta, Sydney, Melbourne, Glasgow, Dublin
# http://www.mapdevelopers.com/geocode_bounding_box.php
twitter_stream.filter(locations=[-123.17,37.69,-122.33, 37.93,-0.35,51.38,0.15,51.67,-118.67,33.70,-118.16,34.34,-87.94,41.64,-87.52,42.02,
    -96.999,32.62,-96.46,33.02,-75.28,39.87,-74.96,40.14,-2.3,53.4,-2.15,53.54,-95.79,29.52,-95.01,30.11,-77.12,38.80,-76.91,38.995,-79.64,43.58,
    -79.12,43.86,-71.19,42.23,-70.92,42.4,-123.17,37.69,-122.33,37.93,-84.55,33.65,-84.29,33.89,150.50,-34.17,151.34,-33.42,-80.74,28.04,-80.58,28.2,
    -4.39,55.78,-4.07,55.93,-6.45,53.22,-6.04,53.43],languages=['en'])
