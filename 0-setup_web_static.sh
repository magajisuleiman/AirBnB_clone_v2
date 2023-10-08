#!/usr/bin/env bash
# Sets up webservers for deployment: (Run script on both servers)

# Install Nginx if it's not already installed
if ! command -v nginx &>/dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
web_static_dir="/data/web_static/releases/test"
web_static_shared="/data/web_static/shared"
web_static_current="/data/web_static/current"

sudo mkdir -p "$web_static_dir"
sudo mkdir -p "$web_static_shared"

# Create a fake HTML file
echo "<html><head></head><body>Web Static Test</body></html>" | sudo tee "$web_static_dir/index.html" > /dev/null

# Create or recreate the symbolic link
if [ -L "$web_static_current" ]; then
    sudo rm -f "$web_static_current"
fi
sudo ln -sf "$web_static_dir" "$web_static_current"

# Give ownership to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
nginx_alias_config="location /hbnb_static/ {\n    alias $web_static_current/;\n}\n"
if ! grep -q "$nginx_alias_config" "$nginx_config"; then
    sudo sed -i "/location \/ {/a $nginx_alias_config" "$nginx_config"
fi

# Restart Nginx
sudo service nginx restart
