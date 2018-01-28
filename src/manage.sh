#!/bin/bash

project_dir=~/cybersport

echo "Activating virtual environment..."
. ${project_dir}/env/bin/activate

echo "Executing manage.py..."
sudo python ${project_dir}/src/manage.py $@

if [[ $1 == "migrate" ]]
then
    echo "Synchronizing the slave database..."
    ssh -J 95.163.251.121 student13@192.168.1.25 ~/shell/synchronize-slave.sh
fi

echo "Deactivating the virtual environment..."
deactivate