import os
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from first_tweet import get_first_tweet

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/first_tweet', methods=['POST'])
def first_tweet():
  screen_name = request.form['screen_name']
  first_tweet = get_first_tweet(screen_name)
  return jsonify(first_tweet)

if __name__ == '__main__':
  app.run(debug='DEBUG_MODE' in os.environ)
