import redis
import hashlib
import os
import re

r = redis.Redis(host='localhost', port=6379, db=0)


def md5hash(cleartext):
    return hashlib.md5(cleartext).hexdigest()


def flushdb(self):
    self.execute_command('FLUSHALL')
    print "redis database flushed. All keys cleared. Keys: %d" % dbsize(r)

def dbsize(self):
    return self.execute_command('DBSIZE')

def doFlushDB():
    flushdb(r)

def getdbsize():
    print "current number of elements in the db: %d" % dbsize(r)
    return dbsize(r)

# some error handling
def isMD5(string):
    if len(string) != 32:
        return False
    elif re.findall(r'([a-fA-F\d]{32})', string):
        return True
    else:
        return False

# read from wordlist and populate database
def pumpwordlistintodb(wordlist):
    with open(wordlist, 'r') as file:
        for i, line in enumerate(file):
            cleartext = line.strip()
            r.set(md5hash(cleartext),cleartext)
            print "added: %s : %s" % (md5hash(cleartext), cleartext)
        print "added %d entries into the database" % (i+1)

def breakhash(md5hashstring):
    if isMD5(md5hashstring):
        finding = r.get(md5hashstring)
        if (finding == None):
            return "not found"
        else:
            return finding
    else:
        return "not an md5 hash"

def populateDB():
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "../wordlists/simple_wordlist.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    pumpwordlistintodb(abs_file_path)
    print "filled "
