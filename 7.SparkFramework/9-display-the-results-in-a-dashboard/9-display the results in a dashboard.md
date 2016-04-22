

#### Tools required:

   * Cloud Foundry command line interface
   
   * glup 
   
   * Mozaik Dashboard Framework


#### Steps required:

    * Build and Deploy the app Locally :
    
      * Build
    
      - Install the Cloud Foundry command line interface
      
      - Install gulp framework
      
      - call gulp build

     * Deploy
    
      - call $ cf push from your terminal 

     * Enter Message Hub Credentials in Notebook :

        - Click the Twitter-Spark-Watson-Dashboard app from your bluemix dashboard.
        
        - Click Environment Variables.

        - Copy and paste the 3 Message Hub credentials (api_key, user, and password), replacing the XXX’s in the  Scala notebook .
