# Installing Python
The WhatsApp chatbot is written in Python. We'll install Python, pip, Flask, and Twilio

## Servers
* Web-01: 54.226.168.231
* Web-02: 34.201.82.203
* lb: 34.139.237.184
* ssh -i ~/.ssh/id_rsa ubuntu@

## Commands:
* sudo apt-get install -y python3
* sudo apt-get install -y python3-pip
* sudo pip install Flask
* sudo pip install twilio flask requests
* sudo apt-get update -y && sudo apt-get upgrade -y

### Considerations:
* We chose not to install Python env due to servers memory restrains
