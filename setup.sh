#!/bin/bash
sudo apt-get update
sudo pip install pip --upgrade
sudo pip install virtualenv
virtualenv ~/.env
source ~/.env/bin/activate
xargs sudo apt-get install -y < pkglist
pip install -r requirements.txt
mysql-ctl start
mysql -u root -e "CREATE DATABASE demo CHARACTER SET UTF8;"
mysql -u root -e "CREATE USER demouser@localhost IDENTIFIED BY 'demo1234';"
mysql -u root -e "GRANT ALL PRIVILEGES ON demo.* to demouser@localhost;"
mysql -u root -e "FLUSH PRIVILEGES;"
~/workspace/seidm/manage.py migrate
