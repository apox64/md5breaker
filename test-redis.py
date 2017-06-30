import redis
import hashlib

r = redis.Redis(host='localhost', port=6379, db=0)


def md5hash(cleartext):
    return hashlib.md5(cleartext).hexdigest()


def flushdb(self):
    self.execute_command('FLUSHALL')
    print "redis database flushed. All keys cleared. Keys: %d" % dbsize(r)


def dbsize(self):
    return self.execute_command('DBSIZE')


def pumpwordlistintodb(wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            cleartext = line.strip()
            r.set(md5hash(cleartext),cleartext)
            print "added: %s : %s" % (md5hash(cleartext), cleartext)


flushdb(r)
pumpwordlistintodb('simple_wordlist.txt')
print "current number of elements in the db: %d" % dbsize(r)
