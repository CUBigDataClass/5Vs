
#### Steps required:


    * built a custom Spark Streaming receiver for Message Hub using Kafka 0.9 
    
    * the Receiver must implement the following lifecycle methods:

     - onStart: called when the receiver is started. Starts a new Thread that will poll MessageHub for new messages and store them in Spark’s memory.
     
     - onStop: called when the receiver is stopped. Cleans up all resources and stops the Thread.
     
     - check (KafkaInputDStream.scala code)
