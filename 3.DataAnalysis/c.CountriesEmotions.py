# -*- coding: utf-8 -*-
import tweepy
import json
import pymongo
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.stem.porter import PorterStemmer
import operator
import csv

# install python 2.7
# install tweepy, $ sudo pip install tweepy
# install pymongo, $ sudo pip install pymongo
# install NLTK, $ sudo pip install -U nltk
# run this program as $ python CountriesEmotions.py
# it will keep running until the user presses ctrl+c to exit
# to see the output, open the terminal and type $ mongo ds019980.mlab.com:19980/worldemotion -u <dbuser> -p <dbpassword>
# in the opened mongo shell type: $ use worldemotion  $ db.emotions.find().pretty()

consumer_key = '***'
consumer_secret = '***'
access_token = '***'
access_secret = '***'

# use consumer keys and access tokens for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
# create the actual interface, using authentication
api = tweepy.API(auth)

# This function is to create a list of certain emotion keywords from a file
def createEmotionList(key,matrix):
    emotionlist=[]
    for row in matrix:
        emotionlist.append(row[key].decode('unicode_escape'))
    return emotionlist

# This function is to get a list of tokens from the tweet text
def token_words(text):
    tknzr = TweetTokenizer()
    tokens=tknzr.tokenize(text)
    return tokens

# This function is to apply the stemmer on the tokens list
def stem_words(tokens):
    st = PorterStemmer()
    stemmed_words= [st.stem(word) for word in tokens]
    return stemmed_words

#This function is to classify the tweet into one of the emotion categories
def classify_tweet(stemmed_tokens):
    emotionCnt={'Happy':0,'Sad':0,'Anger':0,'Fear':0,'Surprise':0,'Disgust':0}  
    
    for token in stemmed_tokens:
        if token in happyList: emotionCnt['Happy'] +=1
        elif token in sadList: emotionCnt['Sad'] +=1
        elif token in angerList: emotionCnt['Anger'] +=1
        elif token in fearList: emotionCnt['Fear'] +=1
        elif token in surpList: emotionCnt['Surprise'] +=1
        elif token in disgList: emotionCnt['Disgust'] +=1
    print('happy count:',emotionCnt['Happy'])
    print('sad count:',emotionCnt['Sad'])
    print('anger count:',emotionCnt['Anger'])
    print('fear count:',emotionCnt['Fear'])
    print('surprise count:',emotionCnt['Surprise'])
    print('disgust count:',emotionCnt['Disgust'])
    
    max_emotion=max(emotionCnt.keys(), key=(lambda k: emotionCnt[k]))
    tweet_emotion= 'Neutural' if max(emotionCnt.values()) == 0 else max_emotion
    return tweet_emotion

class Listener(tweepy.StreamListener):
    
    def __init__(self, api):
        super(tweepy.StreamListener, self).__init__()
        self.api = api
        # create an instance of the Mongodb client with a connection to our database on Mongolab.
        client = pymongo.MongoClient("ds019980.mlab.com",19980)
        #client = pymongo.MongoClient()
        # create a database called worldemotion
        self.db=client['worldemotion']  
        # MongoLab has user authentication
        self.db.authenticate("***", "***")

    # this function gets called every time a new tweet is received on the stream
    def on_data(self, data):   
        #convert the tweet data to a json object          
        tweet=json.loads(data)                   
        print (tweet['text'])
        
        # get a list of lowercase tokens from the tweet text
        tokens=token_words(tweet['text'].lower())
        print(tokens)

        # apply the stemmer on the tokens list
        stemmed_tokens=stem_words(tokens)
        print(stemmed_tokens)

        # classify the tweet into one of the emotion categories
        tweet_emotion=classify_tweet(stemmed_tokens)
        print(tweet_emotion)
        
        # insert only the interested tweet data into the (emotions) collection
        if tweet_emotion != 'Neutural' and tweet['place'] != None:
            self.db.emotions.insert( { 'created_at' : tweet['created_at'], 'text' : tweet['text'], 'location_name' : tweet['place']['full_name'], 'country_code' : tweet['place']['country_code'], 'tweet_emotion' : tweet_emotion } )

    def on_error(self, status):
        print ("ERROR")
        print (status)
        return True         #To continue listening

    def on_timeout(self):
        print ("Timeout")
        return True         #To continue listening


if __name__ == '__main__':
    # to create a matrix of emotion lists from EmotionsWords.csv file
    with open('EmotionsWords.csv','rU') as csvfile:
        emotionsMatrix = list(csv.DictReader(csvfile))
    csvfile.close()

    # function calls to generate the six emotion lists from the emotion matrix
    happyList=createEmotionList('happy',emotionsMatrix)
    sadList=createEmotionList('sad',emotionsMatrix)
    angerList=createEmotionList('anger',emotionsMatrix)
    fearList=createEmotionList('fear',emotionsMatrix)
    surpList=createEmotionList('surprise',emotionsMatrix)
    disgList=createEmotionList('disgust',emotionsMatrix)
    #print(disgList)
        
    while True:
        try:
            # create the listener and connect to the Twitter stream
            twitter_stream = tweepy.streaming.Stream(auth, Listener(api))
            # filter the Twitter Stream using the largest bounding box to retrieve tweets around the world (any geotagged tweet)
            twitter_stream.filter(locations=[-180,-90,180,90],languages=['en'])
        except KeyboardInterrupt:
        #user pressed ctrl+c -- get ready to exit the program
            break
        except: 
            continue
