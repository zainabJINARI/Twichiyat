#!/bin/bash

# Ensure pip is installed and upgrade pip
python -m ensurepip --upgrade
python -m pip install --upgrade pip

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run any other custom commands if necessary
