# This code streams the data from English geotagged tweets and applies a set of sentiment analysis tools
# to categorize tweets into six emotions and stores them in mongodb.
# Then from the extracted emotional tweets, the code finds the common emotion for each country in a periodic manner 
# and stores the results on mongodb in order to visualize the results on the website map.

# -*- coding: utf-8 -*-
import tweepy
import json
import pymongo
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.stem.porter import PorterStemmer
import operator
import csv
from senti_classifier import senti_classifier
import time, threading

# install python 2.7
# install tweepy, $ sudo pip install tweepy
# install pymongo, $ sudo pip install pymongo
# install NLTK, $ sudo pip install -U nltk
# download senti_classifier from https://github.com/kevincobain2000/sentiment_classifier/tree/master/src/senti_classifier
# then install it, $ sudo python setup.py install
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

# This function to create a list of certain emotion keywords from a file
def createEmotionList(key,matrix):
    emotionlist=[]
    for row in matrix:
        emotionlist.append(row[key].decode('unicode_escape'))
    return emotionlist

# This function to get a list of tokens from the tweet text
def token_words(text):
    tknzr = TweetTokenizer()
    tokens=tknzr.tokenize(text)
    return tokens

# This function to apply the stemmer on the tokens list
def stem_words(tokens):
    st = PorterStemmer()
    stemmed_words= [st.stem(word) for word in tokens]
    return stemmed_words

#This function to classify the tweet into one of the six emotion categories
def classify_tweet(stemmed_tokens, sentences):
    pos_score, neg_score = senti_classifier.polarity_scores(sentences)
    print pos_score, neg_score

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
    
    if max(emotionCnt.values()) == 0 :
        tweet_emotion= 'Neutural' 
    elif pos_score >= neg_score:
        if max_emotion =='Happy' or max_emotion=='Surprise':
            tweet_emotion = max_emotion
        else:
            tweet_emotion= 'Neutural' 
    else: 
        if max_emotion =='Anger' or max_emotion=='Fear' or max_emotion=='Disgust' or max_emotion=='Sad' or max_emotion=='Surprise':
            tweet_emotion = max_emotion
        else:
            tweet_emotion = 'Neutural' 

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
        lowerText= tweet['text'].lower()                 
        print (lowerText)

        # get a list of lowercase text of the tweet text
        sentences = []
        sentences.append(lowerText) 

        # get a list of tokens from the tweet text
        tokens=token_words(lowerText)

        # apply the stemmer on the tokens list
        stemmed_tokens=stem_words(tokens)

        # classify the tweet into one of the emotion categories
        tweet_emotion=classify_tweet(stemmed_tokens, sentences)
        print(tweet_emotion)
        
        # insert only the interested tweet data with the resulted emotion into the (emotions) collection
        if tweet_emotion != 'Neutural' and tweet['place'] != None:
            self.db.emotions.insert( 
                {   'created_at' : tweet['created_at'],
                    'text' : tweet['text'],
                    'location_name' : tweet['place']['full_name'],
                    'country_code' : tweet['place']['country_code'],
                    'tweet_emotion' : tweet_emotion 
                } 
            )

    def mongoQuery(self):
        print(time.ctime())

        # apply Mongodb aggregation query to find the count of each emotion for each country
        country_emotions=self.db.emotions.aggregate(
            [
                {'$group': {'_id' : {'country': '$country_code', 'emotion': '$tweet_emotion'}, 'total' : {'$sum' : 1}}},
                {'$sort': {'_id': 1}},
                {'$project' : {'country' : '$_id.country', 'emotion' : '$_id.emotion', 'emotion_count' : '$total', '_id' : 0}}
            ]
        )

        # store the emotions result for each country with the current time in a new collection (countryEmotion) 
        result1=[]
        ctime=time.ctime()
        result1.append({'current_time': ctime})
            
        for document in country_emotions:
            result1.append(document)
            
        self.db.countryEmotion.insert({'country_emotions':result1})

        # apply Mongodb aggregation query to find the common emotion for each country
        country_emotion=self.db.emotions.aggregate(
            [
                {'$group': {'_id' : {'country': '$country_code', 'emotion': '$tweet_emotion'}, 'emotionCount' : {'$sum' : 1}}},
                {'$group': {'_id' :'$_id.country', 'maxEmotionCount' : {'$max' : '$emotionCount'}}},
                {'$sort': {'_id': 1}},
                {'$project' : {'country' : '$_id', 'emotion' : '$_id.emotion', 'maxEmotionCount' : '$maxEmotionCount', '_id' : 0}}
            ]
        )

        # store the common emotion result for each country with the current time in the collection (countryEmotion) 
        result2=[]
        ctime=time.ctime()
        result2.append({'current_time': ctime})
            
        for document in country_emotion:
            result2.append(document)
            
        self.db.countryEmotion.insert({'country_emotion':result2})

        # run a thread to execute this Mongodb aggregation query on the emotions collection every 300 seconds = 5 minutes
        threading.Timer(300, self.mongoQuery).start()

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

    lis=Listener(api)
    
    # run a thread to execute this Mongodb aggregation query on the emotions collection every 300 seconds = 5 minutes
    threading.Timer(300, lis.mongoQuery).start()

    while True:
        try:
            # create the listener and connect to the Twitter stream
            twitter_stream = tweepy.streaming.Stream(auth, lis)
            # filter the Twitter Stream using the largest bounding box to retrieve tweets around the world (any geotagged tweet)
            twitter_stream.filter(locations=[-180,-90,180,90],languages=['en'])
        except KeyboardInterrupt:
        #user pressed ctrl+c -- get ready to exit the program
            break
        except: 
            continue
