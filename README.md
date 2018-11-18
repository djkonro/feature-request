# Feature request app

This is a python web application  which provides the ability
to record the details of a feature request made by by clients. Though 
there are some limitations such as hard-coded client
and priority data, there are some useful actions that can be
carried out.

## Technologies
- Python 3.6
- Flask
- SQLAlchemy
- Knockout JS
- Docker

## Development
- The application backend provides a semi RESTful API with CRUD methods,
used to interact with the database. There are also utility modules for setting
up the database, app creation and handling client priority updates.
- The app frontend utilizes Bootstrap, Ajax, jQuery and Knockout JS to provide 
a responsive interface.
- It also includes unit tests to ensure proper functioning of our api methods.
- Docker is used to facilitate deployments of the application.

## Installing and Running

Clone this repository
```
$ git clone https://github.com/djkonro/feature-request.git
```

### Using docker
After installing [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/)
```
$ cd feature-request
$ sudo docker-compose build
$ sudo docker-compose up
```

### Running Locally

Setup [Mysql database](https://www.mysql.com/)
Run the following commands from the Mysql prompt

```
mysql> CREATE DATABASE appdb;
mysql> CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'password';
mysql> GRANT ALL ON appdb.* TO 'appuser'@'localhost';
```

Create and activate virtual environment
```
$ cd feature-request
$ virtualenv -p python3 pyenv
$ source pyenv/bin/activate
```

Install requirements
```
$ cd feature_request
$ pip install -r requirements.txt
```

Run
```
$ python feature_request.py dev
```

Open url in browser `http://127.0.0.1:5000/`

### Running tests
```
$ python -m unittest tests/feature_request_test.py
```
