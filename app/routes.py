from flask import render_template
from flask import jsonify
from flask import request

from flask_cors import CORS, cross_origin

from logic import breakhash
from logic import getdbsize
from logic import doFlushDB
from logic import initDB
from logic import md5hash
from logic import add_to_database

from app import app

@app.route('/', methods = ['GET'])
@cross_origin()
def index():
    return render_template("index.html")

@app.route('/about', methods = ['GET'])
@cross_origin()
def about():
    return render_template("about.html")

@app.route('/md5/<md5hashstr>', methods = ['GET'])
@cross_origin()
def breakmd5hash(md5hashstr):
    message = {
        'hash' : md5hashstr,
        'clear' : breakhash(md5hashstr)
    }
    return jsonify(message)

@app.route('/result', methods = ['POST'])
@cross_origin()
def resultsomething():
    clear = request.form.getlist('md5hash')[0]
    return render_template("index.html", result = breakhash(clear))

@app.route('/db/add/<clear>')
@cross_origin()
def add_md5(clear):
    add_to_database(clear)
    getdbsize()
    message = {
        'hash' : md5hash(clear),
        'clear' : clear
    }
    return jsonify(message)

@app.route('/db/flush', methods = ['GET'])
@cross_origin()
def flushDatabase():
    doFlushDB()
    message = {
        'status' : 'flushed',
        'entries' : getdbsize()
    }
    return jsonify(message)

@app.route('/db/init', methods = ['GET'])
@cross_origin()
def init():
    initDB()
    message = {
        'status' : 'initialized',
        'entries' : getdbsize()
    }
    return jsonify(message)
