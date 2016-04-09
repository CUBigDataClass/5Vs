### Website
	* deployed on Amazon EC2 instance using Elastic Beanstalk
    
#### Tools required:
	* Django==1.9.2
	* a python virtualenv with necessary dependencies is in the directory **ebvirt**

#### Steps to run locally:
	* (start from the 5Vs/5.Website)

	*  ```source eb-virt/bin/activate```

	*  ```(eb-virt)  ~/5Vs/5.Website python manage.py runserver```

	* ```Django version 1.9.2, using settings 'ebdjango.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Not Found: /
[15/Feb/2016 20:14:09] "GET / HTTP/1.1" 200 1767
Ctrl+C```

	* server should be started and exist at http://127.0.0.1:8000/
    
