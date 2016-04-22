



#### Tools required:

    * Apache Spark Object Storage service in your Bluemix account
    

#### Steps required:

    * create a StreamingContext with a Batch Time Interval of 5 seconds :
    
    ssc = new StreamingContext( sc, Seconds(5) )
    
    ssc.checkpoint(kafkaProps.getConfig( MessageHubConfig.CHECKPOINT_DIR_KEY ));
    
    * Configure Spark Streaming Checkpointing to use Swift Object Storage
    
    Url must have the following format: swift://notebook.<name>/<container> where:

    <name> is an abritrary string, like spark, that you’ll use later in the hadoop configuration step
    
    <container> is the name of the container or folder where all the files will live, like ssc.
    
   *  set the following key/values pair in the hadoopConfiguration hashmap (check scala code hadoopConfiguration.scala)
   
   * enter the proper credentials in your Scala Notebook :

      - Click  Apache Spark Object Storage service from your Bluemix dashboard.
      
      - Click Service Credentials.
      
      - In Spark Streaming checkpointing configuration section, replace the XXX’s in the Scala notebook’Copy and paste the 3 object storage credentials (Project_ID, userId, and password).
