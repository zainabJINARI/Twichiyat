#!/bin/bash

# Ensure pip is installed and upgrade pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.10 get-pip.py

# Upgrade pip and install dependencies
python3.10 -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Collect static files
python3.10 manage.py collectstatic --noinput