from flask import render_template
from flask import jsonify
from flask import request

from mainlogicredis import breakhash
from mainlogicredis import getdbsize
from mainlogicredis import doFlushDB
from mainlogicredis import initDB

from app import app

@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@app.route('/about', methods = ['GET'])
def about():
    return render_template("about.html")

@app.route('/md5/<md5hashstr>', methods = ['GET'])
def breakmd5hash(md5hashstr):
    message = {
        'hash' : md5hashstr,
        'clear' : breakhash(md5hashstr)
    }
    return jsonify(message)

@app.route('/result', methods = ['POST'])
def resultsomething():
    clear = request.form.getlist('md5hash')[0]
    return render_template("index.html", result = breakhash(clear))

@app.route('/database/flush', methods = ['GET'])
def flushDatabase():
    doFlushDB()
    message = {
        'status' : 'flushed',
        'entries' : getdbsize()
    }
    return jsonify(message)

@app.route('/database/init', methods = ['GET'])
def init():
    initDB()
    message = {
        'status' : 'initialized',
        'entries' : getdbsize()
    }
    return jsonify(message)
