# md5breaker

[![Build Status](https://travis-ci.org/apox64/md5breaker.svg?branch=master)](https://travis-ci.org/apox64/md5breaker)

Simple md5 breaking microservice written in python using Flask and redis. Offers an HTML frontend and an API.

---

## Usage

1. put some wordlist files in `/wordlists`
2. `/db/init`
3. `/md5/21232f297a57a5a743894a0e4a801fc3` will give you the cleartext `admin` (JSON)

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

## Run with Docker (recommended)

1. clone the repo: `git clone https://github.com/apox64/md5breaker.git`
2. install [docker-compose](https://docs.docker.com/compose/install/)
3. run `docker-compose build` and `docker-compose up`

---

## Run without Docker

1. install a database server: `sudo apt-get install redis-server` (you can verify if it's running with `netstat -tulpn`, it should run on port **6379** (default))
2. go to `app/logic.py` and change `host='redis'` to `host='127.0.0.1'`
3. verify connection via `redis-cli ping` (should return `PONG`)
4. install the [requirements](https://github.com/apox64/md5breaker/blob/master/requirements.txt) with `pip install -r requirements.txt`
5. run `python run.py` *(alternatively you can first* `export FLASK_APP=run.py` *and then run* `flask run` *)*
