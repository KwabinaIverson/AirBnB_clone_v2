#!/usr/bin/env bash

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_text="location /hbnb_static/ {\n\talias /data/web_static/current/;\n\tindex index.html;\n}\n"
sudo sed -i "/server_name _;/a $config_text" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0
