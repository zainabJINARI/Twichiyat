#!/bin/bash


# Ensure pip is installed and upgrade pip
python3.9 -m ensurepip --upgrade

python3.9 -m pip install --upgrade pip setuptools wheel
# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files
pip install --disable-pip-version-check --target . --upgrade -r requirements.txt
# Run any other custom commands if necessary

# Install necessary build tools

python3.9 manage.py collectstatic --noinput

