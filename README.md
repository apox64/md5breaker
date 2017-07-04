# md5breaker-python
Simple md5 breaking service written in python using Flask and redis. Offers an HTML frontend and an API.

---

## Endpoints
currently available endpoints (routes) are:
  * /
  * /about
  * /result (POST)
  * /md5/`<md5hashstr>`
  * /db/flush
  * /db/init
  * /db/add/`<cleartext>` (this will hash the cleartext and add it to the database)

---

## Installation

1. clone the repo: `git clone https://github.com/apox64/md5breaker-python.git`
---
the following part is only necessary, when you don't use docker ...
2. install a database server: `sudo apt-get install redis-server` (you can verify if it's running with `netstat -tulpn`, it should run on port **6379** (default))
3. install Flask `pip install flask` and `sudo apt-get install python-flask`
4. run `python run.py` *(alternatively you can first* `export FLASK_APP=run.py` *and then run* `flask run` *)*
---

## Docker

---
**docker doesn't work properly yet** (containers don't talk to each other)

5. install docker-compose
6. run `docker-compose build` and `docker-compose run`

alternatively:
5. build Docker container from Dockerfile:
`docker build -t md5breaker-python:latest .`
6. run Docker container:
`docker run -d -p 5000:5000 --name md5breaker-python md5breaker-python`
