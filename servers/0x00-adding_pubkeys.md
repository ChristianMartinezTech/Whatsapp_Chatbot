# First steps: SSH server access
4 people in the team need access to the servers. The fist step to setting up the servers is to give them access. 

In Ubuntu servers, the .ssh/ folder has the authorized_keys. Which is the file where the public keys need to be added.

## Servers
* Web-01: 54.226.168.231
* Web-02: 34.201.82.203
* lb: 54.226.106.185

## Commands:
* ssh -i ~/.ssh/id_rsa ubuntu@{server_id}
* cd .ssh/
* vim authorized_keys
* i
* ***add the peer keys***
* cat authorized_keys
* Ctrl + d to close connection
