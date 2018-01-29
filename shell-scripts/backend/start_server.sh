#!/bin/bash

project_dir=~/cybersport

uwsgi --ini ${project_dir}/nginx/cybersport_uwsgi.ini

sudo systemctl restart nginx