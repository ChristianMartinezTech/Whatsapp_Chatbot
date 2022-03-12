# Installing Nginx
Nginx is the application that listens and respond to HTTP requests.  

Both Web servers have Niginx installed and inconjunction with Gunicorn, serve the Python content.

## Servers
* Web-01: 54.226.168.231
* Web-02: 34.201.82.203
* lb: 34.139.237.184 (**This is a web server without Nginx**)
* ssh -i ~/.ssh/id_rsa ubuntu@

## Commands:
* sudo apt-get update -y && sudo apt-get upgrade -y
* sudo apt-get -y install nginx
* sudo service nginx restart

### Considerations:
* Nginx listens to the port 80 by default
* curl -sI {server_ip} to check nginx is properly installe and active
* Not installed on Load balancer
