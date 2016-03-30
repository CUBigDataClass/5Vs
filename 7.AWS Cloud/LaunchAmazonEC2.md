### Launch an Amazon EC2 instance (virtual server) for our project 


#### Steps applied:
[x] ** instance type** : T2 micro server. When our application needs to have a larger server, we can upgrade it later.

[x] ** EBS vlume** : 30 GB to be used for the database permanent storage.

[x] The chosen security groups:
    - HTTP, port 80
    - SSH, port 22
    - custom TCP, port 27017 (for MongoDB)

[x] Our public key for this instance on AWS is **5Vs** and the private key is saved in a safe place :)

[x] The server is running now and the instance name is **5Vs**