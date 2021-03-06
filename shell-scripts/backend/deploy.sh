#!/bin/bash

project_dir=~/cybersport
return_dir=$(pwd)

if [[ $1 == "create" ]] # create for first time
then
	# Clone code from repository
    echo "Cloning repository..."
	git clone https://github.com/murnat98/cybersport.git ${project_dir}

	# Create virtual environment
	echo "Creating virtual environment..."
	python3.6 -m venv ${project_dir}/env

	sudo ln -s ${project_dir}/nginx/cybersport.conf /etc/nginx/conf.d/
else
	cd ${project_dir}

    echo "Pull changes from repository..."
	git pull
	echo "Migrating changes to database..."
    ./src/manage.sh migrate
    ./src/manage.sh collectstatic
    # Add testing

    cd ${return_dir}
fi

# install requirements
echo "Installing project requirements..."
. ${project_dir}/env/bin/activate
pip install -r ${project_dir}/requirements.txt
