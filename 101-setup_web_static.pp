exec { 'server setup pt 1':
  command  => 'sudo apt-get -y update && sudo apt-get -y install nginx && sudo service nginx start && sudo mkdir -p /data/web_static/shared/ && sudo mkdir -p /data/web_static/releases/test/ && echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html > /dev/null',
  provider => shell,
}

exec { 'server setup pt 2':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_stati    c/current && sudo chown -R ubuntu:ubuntu /data/ && sudo sed -i '44i \\n\tlocation /hbn    b_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/defa    ult && sudo service nginx restart',
  provider => shell,
}
