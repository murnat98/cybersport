#!/bin/bash

project_dir=~/cybersport

uwsgi --ini ${project_dir}/nginx/cybersport_uwsgi.conf

sudo systemctl restart nginx