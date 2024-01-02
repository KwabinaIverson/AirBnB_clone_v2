#!/usr/bin/env bash

# Install Nginx if it's not already installed
apt-get update
apt-get -y install nginx

# Create the necessary directory structure
mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file for testing
echo '<html> <head> </head> <body> Holberton School </body> </html>' > /data/web_static/releases/test/index.html

# Correctly manage symbolic links
ln -snf /data/web_static/releases/test /data/web_static/current

# Set ownership and permissions
chown -hR ubuntu:ubuntu /data

# Update Nginx configuration
sed -i '51 i \
\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
