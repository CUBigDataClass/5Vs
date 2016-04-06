# -*- coding: utf-8 -*-
import tweepy
import json
import pymongo
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.stem.porter import PorterStemmer
import operator

# install python 2.7
# install tweepy $ sudo pip install tweepy
# install mongoDB http://bit.ly/1Xpkq1e
# install pymongo $ sudo pip install pymongo
# install NLTK $ sudo pip install -U nltk
# run the mongod server then run this program as: python TweetsMongoDB.py
# it will keep running until the user presses ctrl+c to exit
# to see the output: open the mongo shell then type: $ use twitterDB  $ db.emotions.find().pretty()

consumer_key = '***'
consumer_secret = '***'
access_token = '***'
access_secret = '***'

# use consumer keys and access tokens for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
# create the actual interface, using authentication
api = tweepy.API(auth)

happyList=['funny','happy','cheerful','alive','excited','joyful','carefree', 'motivated', 'playful', 'delighted','glad','lucky',':)','=)',':-)',':D',':3',u'\ude0d']
sadList=['sad','grief','lonely','disappointed','hopeless','depressed','miserable','lost','bored','regretful',':(','=(',':^(',u'\ude29']
angerList=['angry','furious','annoyed','frustrated','enraged','irritable','resentful','mad','raging','livid','bitter','seething','>:S','>:',':@',u'\ude20']
fearList=['panicked','restless','anxious','frantic','nervous','hesitant','terrified','tense','timid','afraid','frightened','worried','threatened','fearful','horrified','shaky','scary',':-o',':$','o_O',u'\ude28']

def token_words(text):
    tknzr = TweetTokenizer()
    tokens=tknzr.tokenize(text)
    return tokens

def stem_words(tokens):
    st = PorterStemmer()
    stemmed_words= [st.stem(word) for word in tokens]
    return stemmed_words

def classify_tweet(stemmed_tokens):
    emotionCnt={'Happy':0,'Sad':0,'Anger':0,'Fear':0}
    
    for token in stemmed_tokens:
        if token in st_happyList: emotionCnt['Happy'] +=1
        if token in st_sadList: emotionCnt['Sad'] +=1
        if token in st_angerList: emotionCnt['Anger'] +=1
        if token in st_fearList: emotionCnt['Fear'] +=1
    print('happy count:',emotionCnt['Happy'])
    print('sad count:',emotionCnt['Sad'])
    print('anger count:',emotionCnt['Anger'])
    print('fear count:',emotionCnt['Fear'])

    max_emotion=max(emotionCnt.keys(), key=(lambda k: emotionCnt[k]))
    tweet_emotion= 'Neutural' if max(emotionCnt.values()) == 0 else max_emotion

    return tweet_emotion

class Listener(tweepy.StreamListener):
    
    def __init__(self, api):
        super(tweepy.StreamListener, self).__init__()
        self.api = api

        # create an instance of the Mongodb client
        client = pymongo.MongoClient()
        # create a database called twitterDB
        self.db=client['twitterDB']  

    # this function gets called every time a new tweet is received on the stream
    def on_data(self, data):   
        #convert the tweet data to a json object          
        tweet=json.loads(data)                   
        
        # get a list of lowercase tokens from the tweet text
        tokens=token_words(tweet['text'].lower())
        print(tokens)
        #print([token.encode(encoding='UTF-8') for token in tokens])

        # apply the stemmer on the tokens list
        stemmed_tokens=stem_words(tokens)
        print(stemmed_tokens)

        #classify the tweet into one of the emotion categories
        tweet_emotion=classify_tweet(stemmed_tokens)
        print(tweet_emotion)
        
        #insert only the interested tweet data into the (emotions) collection
        self.db.emotions.insert( { 'created_at' : tweet['created_at'], 'text' : tweet['text'], 'location_name' : tweet['place']['name'], 'location_coordinates' : tweet['place']['bounding_box']['coordinates'], 'tweet_emotion' : tweet_emotion } )

    def on_error(self, status):
        print ("ERROR")
        print (status)
        return True         #To continue listening

    def on_timeout(self):
        print ("Timeout")
        return True         #To continue listening

if __name__ == '__main__':
    try:
        st_happyList=stem_words(happyList)
        st_sadList=stem_words(sadList)
        st_angerList=stem_words(angerList)
        st_fearList=stem_words(fearList)

        # create the listener and connect to the Twitter stream
        twitter_stream = tweepy.streaming.Stream(auth, Listener(api))

        # filter the Twitter Stream using location bounding boxes to retrieve tweets around the following cities in the following order: 
        # New York City, London, Los Angeles, Chicago, Dallas, Philadelphia, Manchester, Houston,
        # Washington D.C., Toronto, Boston, San Francisco, Atlanta, Sydney, Melbourne, Glasgow, Dublin
        twitter_stream.filter(locations=[-123.17,37.69,-122.33, 37.93,-0.35,51.38,0.15,51.67,-118.67,33.70,-118.16,34.34,-87.94,41.64,-87.52,42.02,
        -96.999,32.62,-96.46,33.02,-75.28,39.87,-74.96,40.14,-2.3,53.4,-2.15,53.54,-95.79,29.52,-95.01,30.11,-77.12,38.80,-76.91,38.995,-79.64,43.58,
        -79.12,43.86,-71.19,42.23,-70.92,42.4,-123.17,37.69,-122.33,37.93,-84.55,33.65,-84.29,33.89,150.50,-34.17,151.34,-33.42,-80.74,28.04,-80.58,28.2,
        -4.39,55.78,-4.07,55.93,-6.45,53.22,-6.04,53.43],languages=['en'])
        
    except KeyboardInterrupt:
        #user pressed ctrl+c -- get ready to exit the program
        pass
