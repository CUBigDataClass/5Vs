### Data Analysis
    Apply sentiment analysis on a stream of tweets to categorize each tweet to a specific emotion then store results in mongoDB

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
    
    * install mongoDB http://bit.ly/1Xpkq1e
	
	* install pymongo $ sudo pip install pymongo

	* install NLTK $ sudo pip install -U nltk
	
	* run the mongod server then run this program as: $ python TweetsMongoDB.py and it will keep running until the user presses ctrl+c to exit
	
	* to see the output: open the mongo shell then type: $ use twitterDB  $ db.emotions.find().pretty()
    
    * don't forget to put your own Twitter access tokens before running the program.

    * To run EmotionsClassifier.py or CountriesEmotion.py , no need to install mongodb on you local machine. Their code will use mongodb on mongolab to store data. To connect to the database , open your terminal and type:
            $ mongo ds019980.mlab.com:19980/worldemotion -u <dbuser> -p <dbpassword>

    * download this Github library: https://github.com/kevincobain2000/sentiment_classifier/tree/master/src/senti_classifier

    * Then install it: sudo python setup.py install
    
    * use instruction here if you found problems in installation: https://github.com/kevincobain2000/sentiment_classifier/issues/1 