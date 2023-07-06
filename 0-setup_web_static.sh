#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee -a /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -hR ubuntu:ubuntu "/data"
sudo sed -i "/server_name _;/a\ \n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
