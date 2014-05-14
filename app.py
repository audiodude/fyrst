import os
from flask import Flask

from first_tweet import get_first_tweet

app = Flask(__name__)

@app.route('/<screen_name>')
def first_tweet(screen_name):
  return get_first_tweet(screen_name)['text']
