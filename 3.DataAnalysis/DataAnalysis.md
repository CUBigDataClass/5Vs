### Data Analysis
    Apply sentiment analysis on a stream of tweets to categorize each tweet to a specific emotion then store results. Then from the extracted emotional tweets, the program finds the common emotion for each country 
    and stores the results on mongodb

#### Tools required:
	- Twitter Streaming API
    - Python
    - Tweepy
    - mongodb
    - pymongo
    - NLTK
    - senti_classifier

#### Steps required:
	* create a Twitter app and get access tokens
    
    * install python 2.7
    
    * install tweepy $ sudo pip install tweepy
    
    * install mongoDB http://bit.ly/1Xpkq1e (optional)
	
	* install pymongo $ sudo pip install pymongo

	* install NLTK $ sudo pip install -U nltk

    * if you found any problems related to  NLTK installation:
        enter python,  >> import nltk >> nltk.download() , from the popup window choose and install the missed tool

    * to install senti_classifier, download this Github library: https://github.com/kevincobain2000/sentiment_classifier/tree/master/src/senti_classifier Then install it $ sudo python setup.py install

    * if you get All sentiment scores as (0,0), follow the instructions here: https://github.com/kevincobain2000/sentiment_classifier/issues/1 
	
	* for TweetsMongoDB.py, run the mongod server then run this program as: $ python TweetsMongoDB.py and it will keep running until the user presses ctrl+c to exit
	
	* to see the output: open the mongo shell then type: $ use twitterDB  $ db.emotions.find().pretty()
    
    * don't forget to put your own Twitter access tokens before running the program.

    * To run EmotionsClassifier.py or CountriesEmotion.py , no need to install mongodb on you local machine. Their code will use mongodb on mongolab to store data. To connect to the database , open your terminal and type:
            $ mongo ds019980.mlab.com:19980/worldemotion -u <dbuser> -p <dbpassword>
 