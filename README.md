# flask-api-demo
A demo to create API's via flask

## Usage
```
## Please check the versions and upgrade virtual env
python3
pip3 --version
pip3 install --upgrade virtualenv

## Create virtual env
create virtual env  flask_demo
virtualenv -p python3 flask_demo

## Activate virtual env
activate flask_demo
source flask_demo/bin/activate

## Install Flask
install flask
pip install flask

## Check installation of flask and its ready to use
try
  python3
  >>> import flask
  >>>
If you do not get any errors, then you imported Flask successfully.

## Please install all the requirements:
pip install -r requirements.txt

## To create just Flask stattic API please check:
task-app/app.py
# To execute the code, try:
python task-app/app.py

## To see combination of REST API With Flask & SQL Alchemy:
flask-sql/app.py
# To execute the code, try:
python flask-sql/app.py

## You can test the API's with postman collection. Please import it for ready to use:
Fask-API-Demo.postman_collection.json
