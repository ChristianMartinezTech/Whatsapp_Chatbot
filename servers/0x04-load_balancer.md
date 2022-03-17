# Installing and configuring load balancer (HAproxy)

## Servers
* Web-01: 54.226.168.231
* Web-02: 34.201.82.203
* lb: 54.226.106.185
* ssh -i ~/.ssh/id_rsa ubuntu@

# Install HAproxy load balancer
* sudo apt-get -y install haproxy

# Configure HAproxy using roundrobin, so that it send traffic to web-01 and web-02
* sudo chmod 777 /etc/haproxy/haproxy.cfg
* echo "frontend http_front
    bind *:80
    stats uri /haproxy?stats
    default_backend http_back
backend http_back
    balance roundrobin
    server 2388-web-01 54.226.168.231:80 check
    server 2388-web-02 34.201.82.203:80 check" >> /etc/haproxy/haproxy.cfg

# Restart
sudo service haproxy restart