#!/usr/bin/env bash

. ../env/bin/activate

sudo python manage.py $@

if [[ $1 == "migrate" ]]
then
    ssh -J 95.163.251.121 student13@192.168.1.25 ~/shell/synchronize-slave.sh
fi

deactivate