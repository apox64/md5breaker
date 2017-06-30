from flask import render_template

from mainlogicredis import breakhash
from mainlogicredis import getdbsize
from mainlogicredis import doFlushDB
from mainlogicredis import populateDB

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/md5/<md5hashstr>')
def breakmd5hash(md5hashstr):
    #brokenhash = breakhash(md5hashstr)
    #print brokenhash
    return 'cleartext for \"%s\" : %s' % (md5hashstr, breakhash(md5hashstr))
    #return 'dbsize: %d' % getdbsize()

@app.route('/database/flush')
def flushDatabase():
    doFlushDB()
    return "database flushed."

@app.route('/database/populate')
def populate():
    populateDB()
    return "database populated."
