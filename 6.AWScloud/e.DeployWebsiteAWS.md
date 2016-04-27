### Deploying the Website Using Elastic Beanstalk on AWS: 




##### Steps Applied:

###Website
	* deployed on Amazon EC2 instance using Elastic Beanstalk
    
####Tools required:

	* Django==1.9.2
	* a python virtualenv with necessary dependencies is in the directory **ebvirt**

    
####Steps to deploy to remote: (look http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html for more detailed instructions and troubleshooting)
    * (again, start from 5Vs/5.Website)
    
    * source eb-virt/bin/activate
    
    * pip freeze > requirements.txt (Requirements.txt lets AWS know what python libraries are needed. If no new libraries have been added, this step can be skipped.)
    
    * sudo pip install awsebcli
    * eb init -p python2.7 emotion_map
    * eb create emotion_env
    * eb open
    * 
    * to redeploy: eb deploy
    * 
    

