#!/usr/bin/env bash
# Set up of a web server to deployment a web static.

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow "Nginx HTTP" # Firewall Port 80
sudo chmod '0777' /var/www/html/index.nginx-debian.html

sudo mkdir -p /data/web_static/{releases/test,shared}

echo "
<html>
  <head>
  </head>
  <body>
    Holberton School - Yesid A. López V. --> You're the best programmer.
  </body>
</html>
" > /data/web_static/releases/test/index.html

# symbolik link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/  # give the owner ship to ubuntu and user group
#
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
