# Thie code gets a stream of tweets contains the "Happy" word 

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
            with open('StreamTest.json', 'a') as f:
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
twitter_stream.filter(track=['happy'])
