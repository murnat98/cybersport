#!/bin/bash

sudo yum -y update

# Install python3 an pip3
echo "Installing python3..."
sudo yum -y install yum-utils
sudo yum -y groupinstall development
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
sudo yum -y install python36u
sudo yum -y install python36u-pip


# Install server
echo "Installing nginx..."
sudo yum -y install epel-release
sudo yum -y install nginx

echo "Starting nginx..."
sudo systemctl start nginx
sudo systemctl enable nginx

echo "Installing uWsgi..."
sudo pip3.6 install uwsgi
