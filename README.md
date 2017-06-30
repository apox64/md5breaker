# md5breaker-python
Simple md5 breaking service written in python using Flask and redis. Offers an HTML frontend and an API.

---

## How-To

1. clone the repo: `git clone https://github.com/apox64/md5breaker-python.git`
2. install a database server: `sudo apt-get install redis-server` (you can verify if it's running with `netstat -tulpn`, it should run on port **6379** (default))
3. run `python run.py` *(alternatively you can first* `export FLASK_APP=run.py` *and then run* `flask run` *)*
4. currently available endpoints (routes) are:
  * /
  * /about
  * /result (POST)
  * /md5/`<md5hashstr>`
  * /database/flush
  * /database/populate
