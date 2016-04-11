### Running Mongodb on Amazon AWS: 

We have used [MongoLab](https://mlab.com/aws/), which is a partner that provides an easy way to run and manage MongoDB on Amazon AWS


##### Steps Applied:

	1. create a new account, choose the plan and storage features.

	2. create a new database named *worldemotion*, and provide credentials for the database user.

	3. To connect to the database using its Mongo shell on the cloud, open your terminal and type:

		$ mongo ds019980.mlab.com:19980/worldemotion -u <dbuser> -p <dbpassword>

		>>Also, you can manage the database through MongoLab interface.

	4. To connect to the database from MongoLab in your code with pymongo, you will need the following info:

		* db_name: worldemotion
		* db_user: ***
		* db_password: ***s
		* db_server: ds019980.mlab.com
		* db_port: 19980


