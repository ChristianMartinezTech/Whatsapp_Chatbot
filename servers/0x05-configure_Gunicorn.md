# Configuring Nginx as reverse proxy and Gunicorn


## Servers
* Web-01: 54.226.168.231
* Web-02: 34.201.82.203
* lb: 54.226.106.185
* ssh -i ~/.ssh/id_rsa ubuntu@

# Bind Gunicorn
* gunicorn --bind 0.0.0.0:80 wsgi:app

# Create michi.service
sudo vim /etc/systemd/system/michi.service >> "[Unit]
Description=Gunicorn instance to serve michi.py
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Whatsapp_Chatbot
Environment="PATH=/home/ubuntu/Whatsapp_Chatbot/michibotenv/bin"
ExecStart=/usr/local/bin/gunicorn --workers 3 --bind unix:michi.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target"

# Start and check michi.service
sudo systemctl start michi
sudo systemctl enable michi
sudo systemctl status michi

# Setup nginx
sudo vim /etc/nginx/sites-available/michi >> "server {
    listen 80;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/Whatsapp_Chatbot/michi.sock;
    }
}"
sudo ln -s /etc/nginx/sites-available/michi /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

# Block access to  port 5000
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
