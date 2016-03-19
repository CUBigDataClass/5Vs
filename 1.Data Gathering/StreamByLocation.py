import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json

# Download / install python and tweepy (sudo pip install tweepy)
# Run as: python StreamByLocation.py
# It will keep running until the user presses ctrl+c to exit
# All output stored to TweetsOutput.json (one tweet  per line)
# Text of tweets also printed as recieved 

# Consumer keys and access tokens, used for OAuth
consumer_key = '****'
consumer_secret = '****'
access_token = '****'
access_secret = '****'

class Listener(StreamListener):
 
    # This function gets called every time a new tweet is received on the stream
    def on_data(self, tweet):

        fOut.write(tweet)           
        jtweet=json.loads(tweet)  #Convert the tweet data to a json object   
        #text=jtweet["text"]      #Get the text of the tweet
        #print(text)              #Print it out
        print(json.dumps(jtweet, indent=5)) #pretty-print

    def on_error(self, status):
        print ("ERROR")
        print (status)
        return True         #To continue listening

    def on_timeout(self):
        print ("Timeout")
        return True         #To continue listening

if __name__ == '__main__':
    try:
        #Create a file to store output
        fOut = open("TweetsOutput.json","a") 

        #Create the listener
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        # Create the actual interface, using authentication
        api = tweepy.API(auth)

        #Connect to the Twitter stream
        twitter_stream = Stream(auth, Listener())

        # Filter the Twitter Stream using location bounding boxes to retrieve tweets around the following cities in the same order: 
        # New York City, London, Los Angeles, Chicago, Dallas, Philadelphia, Manchester, Houston,
        # Washington D.C., Toronto, Boston, San Francisco, Atlanta, Sydney, Melbourne, Glasgow, Dublin
        twitter_stream.filter(locations=[-123.17,37.69,-122.33, 37.93,-0.35,51.38,0.15,51.67,-118.67,33.70,-118.16,34.34,-87.94,41.64,-87.52,42.02,
        -96.999,32.62,-96.46,33.02,-75.28,39.87,-74.96,40.14,-2.3,53.4,-2.15,53.54,-95.79,29.52,-95.01,30.11,-77.12,38.80,-76.91,38.995,-79.64,43.58,
        -79.12,43.86,-71.19,42.23,-70.92,42.4,-123.17,37.69,-122.33,37.93,-84.55,33.65,-84.29,33.89,150.50,-34.17,151.34,-33.42,-80.74,28.04,-80.58,28.2,
        -4.39,55.78,-4.07,55.93,-6.45,53.22,-6.04,53.43],languages=['en'])
        
    except KeyboardInterrupt:
        #User pressed ctrl+c -- get ready to exit the program
        pass

    #Close the output file
    fOut.close()
