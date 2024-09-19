#!/bin/bash

# Ensure pip is installed and upgrade pip
python3.10 -m ensurepip --upgrade

python3.10 -m pip install --upgrade pip setuptools wheel

# Install distutils separately
python3.10 -m pip install distutils

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files
python3.10 manage.py collectstatic --noinput
