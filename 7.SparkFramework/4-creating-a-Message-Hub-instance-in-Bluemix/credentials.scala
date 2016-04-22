
 val demo = com.ibm.cds.spark.samples.MessageHubStreamingTwitter
 val config = demo.getConfig()

 config.setConfig("bootstrap.servers","kafka01-prod01.messagehub.services.us-south.bluemix.net:9094,kafka02-prod01.messagehub.services.us-south.bluemix.net:9094,kafka03-prod01.messagehub.services.us-south.bluemix.net:9094,kafka04-prod01.messagehub.services.us-south.bluemix.net:9094,kafka05-prod01.messagehub.services.us-south.bluemix.net:9094")
  
 config.setConfig("api_key","XXXX")
 config.setConfig("kafka.user.name","XXXX")
 config.setConfig("kafka.user.password","XXXX")
 config.setConfig("kafka_rest_url","https://kafka-rest-prod01.messagehub.services.us-  south.bluemix.net:443")
  

 config.setConfig("kafka.topic.tweet","twitter-spark" )
