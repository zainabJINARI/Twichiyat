#!/bin/bash

# Ensure pip is installed and upgrade pip
python3.11 -m ensurepip --upgrade
python3.11 -m pip install --upgrade pip

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files
python3.11 manage.py collectstatic --noinput

# Run any other custom commands if necessary
