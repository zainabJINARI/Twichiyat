#!/bin/bash

# Function to install Python 3.10
install_python() {
    echo "Installing Python 3.10..."
    
    # Add deadsnakes PPA (Ubuntu-specific)
    sudo add-apt-repository ppa:deadsnakes/ppa -y
    sudo apt-get update

    # Install Python 3.10 and pip for Python 3.10
    sudo apt-get install python3.10 python3.10-distutils -y
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    sudo python3.10 get-pip.py

    # Clean up
    rm get-pip.py
}

# Ensure python3.10 is installed
if ! command -v python3.10 &> /dev/null
then
    install_python
fi

# Ensure pip is installed and upgrade pip
python3.10 -m pip install --upgrade pip setuptools wheel

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files
python3.10 manage.py collectstatic --noinput
