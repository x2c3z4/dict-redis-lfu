from redis import StrictRedis as Redis
import redis
import sys
import os

class WordList:
  def __init__(self):
    self.conn = Redis()
    self.CACHE_SIZE = 50
    self.CACHE_KEYS = "words-keys"
    self.CACHE_STORE = "words-store"
    self.WORD_FILE = os.path.join(os.path.expanduser("~"), '.words.txt')

  def _reorganize(self):
    pop_n = self.conn.zcard(self.CACHE_KEYS) - self.CACHE_SIZE
    if pop_n >= 0:
      to_pop = self.conn.zrange(self.CACHE_KEYS, 0, pop_n)
      #print pop_n, to_pop
      self.conn.zremrangebyrank(self.CACHE_KEYS, 0, pop_n)
      for k in to_pop:
        self.conn.hdel(self.CACHE_STORE, k)

  def _add_word(self, key, value):
    result = self.conn.hget(self.CACHE_STORE, key)
    if result:
      self.conn.zincrby(self.CACHE_KEYS, key, 1.0)
    else:
      self._reorganize()
      self.conn.hset(self.CACHE_STORE, key, value)
      self.conn.zadd(self.CACHE_KEYS, 1, key)

  def _get_words(self):
    try:
      words = self.conn.zrevrange(self.CACHE_KEYS, 0, -1, True)
      #hashs = self.conn.hgetall(self.CACHE_STORE)
      #print words
      #print hashs
      return words
    except redis.exceptions.ConnectionError:
      return None

  def dump_console(self):
    if os.path.isfile(self.WORD_FILE):
      with open(self.WORD_FILE, 'r') as f:
        print f.read()

  def write_file(self):
    words = self._get_words()
    if words is None:
      return
    content = '\n'.join(["%d. %s\t %d"%(i, x[0], int(x[1])) for i, x in enumerate(words)])
    with open(self.WORD_FILE, 'w+') as f:
      f.write(content)
      f.write('\n')

  def add_word(self, key):
    try:
      self._add_word(key,key)
      self.write_file()
    except redis.exceptions.ConnectionError:
      return

def main():
  wl = WordList()
  [wl.add_word("test") for i in range(0,1)]
  [wl.add_word("test-0") for i in range(0,2)]
  [wl.add_word("test-1") for i in range(0,3)]
  [wl.add_word("test-2") for i in range(0,4)]
  [wl.add_word("test-3") for i in range(0,5)]
  [wl.add_word("test-4") for i in range(0,6)]
  [wl.add_word("test-5") for i in range(0,7)]
  [wl.add_word("test-6") for i in range(0,8)]
  [wl.add_word("test-7") for i in range(0,9)]
  [wl.add_word("test-8") for i in range(0,10)]
  [wl.add_word("test-9") for i in range(0,11)]

if __name__ == "__main__":
  main()
