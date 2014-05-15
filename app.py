import json
import os

import bmemcached
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

import fyrst

app = Flask(__name__)
mc = bmemcached.Client(
  (os.environ.get('MEMCACHEDCLOUD_SERVERS') or 'localhost').split(','),
  os.environ.get('MEMCACHEDCLOUD_USERNAME'),
  os.environ.get('MEMCACHEDCLOUD_PASSWORD'))

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/first_tweet', methods=['POST'])
def first_tweet():
  screen_name = request.form['screen_name'].encode('utf-8')
  first_tweet_str = mc.get(screen_name)
  if first_tweet_str:
    first_tweet = json.loads(first_tweet_str)
  else:
    first_tweet = fyrst.get_first_tweet(screen_name)
    mc.set(screen_name, json.dumps(first_tweet))

  return jsonify(first_tweet)

@app.route('/tweet', methods=['POST'])
def tweet():
  """Gets a tweet from the Twitter oembed endpoint and caches it."""
  tweet_id = request.form['tweet_id'].encode('utf-8')
  tweet = fyrst.get_tweet(tweet_id)
  return jsonify(tweet)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug='DEBUG_MODE' in os.environ)
