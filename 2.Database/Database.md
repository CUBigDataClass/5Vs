### Database
    Store a stream of tweets filtered by certain locations in mongoDB

#### Tools required:
	- Twitter Streaming API
    - Python
    - Tweepy
    - mongodb
    - pymongo

#### Steps required:
    * create a Twitter app and get access tokens
    
    * install python 2.7
    
    * install tweepy $ sudo pip install tweepy
    
    * install mongoDB http://bit.ly/1Xpkq1e
	
	* install pymongo $ sudo pip install pymongo
	
	* run the mongod server then run this program as: $ python TweetsMongoDB.py and it will keep running until the user presses ctrl+c to exit
	
	* to see the output: open the mongo shell then type: $ use twitterDB  $ db.emotions.find().pretty()
    
    * don't forget to put your own Twitter access tokens before running the program.


	