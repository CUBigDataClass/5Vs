#Original code taken from http://stackoverflow.com/questions/17213991/how-can-i-consume-tweets-from-twitters-streaming-api-and-store-them-in-mongodb

import json
import pymongo
import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        
        self.db = pymongo.MongoClient().test
    
    def on_data(self, tweet):
        self.db.tweets.insert(json.loads(tweet))
    
    def on_error(self, status_code):
        return True # Don't kill the stream
    
    def on_timeout(self):
        return True # Don't kill the stream


twitter_stream = tweepy.streaming.Stream(auth, CustomStreamListener(api))
twitter_stream.filter(track=['happy',':)'], locations = [-122.75,36.8,-121.75,37.8], languages=['en'])