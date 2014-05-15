import os
from TwitterAPI import TwitterAPI


api = TwitterAPI(os.environ['TWITTER_CONSUMER_KEY'],
                 os.environ['TWITTER_CONSUMER_SECRET'],
                 os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                 os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

def get_first_tweet(screen_name):
  count = None
  oldest_id = None
  while count != 0 or count is None:
    params = {
      'screen_name': screen_name,
      'count': 200,
    }
    if oldest_id:
      params['max_id'] = oldest_id
      params['trim_user'] = 1,
    resp = api.request('statuses/user_timeline', params)
    data = resp.response.json()
    count = len(data)
    if count:
      oldest_id = int(data[-1]['id']) - 1
      potential_first_tweet = data[-1]

  return potential_first_tweet
  
def get_tweet(tweet_id):
  resp = api.request('statuses/oembed', {'id': tweet_id, 'omit_script': 1})
  return resp.response.json()
