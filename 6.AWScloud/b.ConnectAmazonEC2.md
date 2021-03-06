### Connect to Amazon EC2 instance: 
You can apply one of the following ways:


#### First: Connecting to your instance using a web browser:
##### Steps applied:
	1. From the Amazon EC2 console, choose Instances in the navigation pane.

	2. Select the instance, and then choose Connect.

	3. Choose A Java SSH client directly from my browser (Java required).

	4. Amazon EC2 automatically detects the public DNS name of your instance and populates Public DNS for you. It 
		also detects the key pair that you specified when you launched the instance. Complete the following, and then choose Launch SSH Client.

		* In User name, enter ec2-user.
		* In Private key path, enter the path to your private key (.pem) file.

	5. Choose Yes to trust the certificate, and choose Run to run the MindTerm client.

	6. Accept the license agreement, confirm setup for your home directory, and confirm setup of the known hosts directory.

	7. A dialog prompts you to add the host to your set of known hosts, choose Yes.

	8. A window opens and you are connected to your instance.

	**Note:**
		Chrome prevents the in-browser Java SSH client from loading. You need to use Firefox, Internet Explorer 9 or higher, or Safari to connect to SSH to your EC2 instances.



#### Second: Connecting to your instance using SSH:
##### Steps applied:
	1. Open an SSH client. 

	2. Locate your private key file (5Vs.pem) and change directories to the location of the private key file.

	3. Use the chmod command to make sure your private key file isn't publicly viewable: $ chmod 400 /path/5Vs.pem 

	4. Use the ssh command to connect to the instance. You'll specify the private key (.pem) file and user_name@public_dns_name
	For our instance: 
		* private key name: 5Vs.pem
		* user_name:ec2-user 
		* public_dns_name : ec2-52-10-133-241.us-west-2.compute.amazonaws.com

	>> The command will be as follow:
		 $ ssh -i ~/path/5Vs.pem ec2-user@ec2-52-10-133-241.us-west-2.compute.amazonaws.com

	>> You'll see a response like the following:
		The authenticity of host 'ec2-198-51-100-1.compute-1.amazonaws.com (10.254.142.33)'
		can't be established.
		RSA key fingerprint is 1f:51:ae:28:bf:89:e9:d8:1f:25:5d:37:2d:7d:b8:ca:9f:f5:f1:6f.
		Are you sure you want to continue connecting (yes/no)?

	5. Enter yes.
	>> You'll see a response like the following.
		Warning: Permanently added 'ec2-198-51-100-1.compute-1.amazonaws.com' (RSA) 
		to the list of known hosts.

	6. Now you are connected to your instance.




