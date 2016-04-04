### Data Analysis
    Apply sentiment analysis on a stream of tweets to categorize each tweet to a specific emotion then store results in mongoDB

#### Tools required:
	- Twitter Streaming API
    - Python
    - Tweepy
    - mongodb
    - pymongo
    - NLTK

#### Steps required:
	* create a Twitter app and get access tokens
    
    * install python 3
    
    * install tweepy $ sudo pip3 install tweepy
    
    * install mongoDB http://bit.ly/1Xpkq1e
	
	* install pymongo $ sudo pip3 install pymongo

	* install NLTK $ sudo pip3 install -U nltk
	
	* run the mongod server then run this program as: $ python3 TweetsMongoDB.py and it will keep running until the user presses ctrl+c to exit
	
	* to see the output: open the mongo shell then type: $ use twitterDB  $ db.emotions.find().pretty()
    
    * don't forget to put your own Twitter access tokens before running the program.