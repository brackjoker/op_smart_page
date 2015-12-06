#!/bin/bash
apt-get install curl
curl http://python-distribute.org/distribute_setup.py | python
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
pip install Django==1.8.6
pip install httplib2==0.9.2
pip install setuptools==18.2
pip install wheel==0.24.0
pip install wsgiref==0.1.2 
