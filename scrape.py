import sys

import fyrst

for tweet in fyrst.get_all_tweets(sys.argv[1]):
  tweet = tweet['text'].encode('utf-8')
  tweet = tweet.replace('\n', ' ')
  print tweet
