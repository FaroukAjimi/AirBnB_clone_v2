#!/usr/bin/env bash
# COMMENT
sudo mkdir -p /data/web_static/releases/test/
sudo bash -c 'echo """<html>
 <head>
 </head>
 <body>
   Holberton School
 </body>
</html>""" > /data/web_static/releases/test/index.html'
ln -fs  /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "46i location /hbnb_static{\nalias /data/web_static/current/;\n}" /etc/nginx/nginx.conf
sudo service nginx restart
