
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py

python3.9 -m pip --version
# Ensure pip is installed and upgrade pip
python3.9 -m pip install --upgrade pip setuptools wheel

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput
