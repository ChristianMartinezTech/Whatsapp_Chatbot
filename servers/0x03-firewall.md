# Installing and configuring Firewall (ufw)

## Servers
* Web-01: 54.226.168.231
* Web-02: 34.201.82.203
* lb: 54.226.106.185
* ssh -i ~/.ssh/id_rsa ubuntu@

* ***Update and upgrade:***
* sudo apt-get -y update && sudo apt-get -y upgrade

* ***UFW shopuld be installed by default in linux:***
* sudo apt-get install -y ufw

* ***Check ufw is installed:***
* sudo ufw status

* ***Allow ports:***
* sudo ufw allow 22/tcp && sudo ufw allow 443/tcp && sudo ufw allow 80/tcp

* ***Check the ports are correctly added:***
* sudo ufw show added

* ***Enable afw:***
* echo "y" | sudo ufw enable

* ***Check ufw is correctly enabled:***
* sudo ufw status

### Considerations:
We installed ufw in both servers and load ballancer. Ports allowed are:
* 22 (SSH)
* 443 (HTTPS SSL)
* 80 (HTTP)
 