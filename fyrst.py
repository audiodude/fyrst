import os
from TwitterAPI import TwitterAPI


api = TwitterAPI(os.environ['TWITTER_CONSUMER_KEY'],
                 os.environ['TWITTER_CONSUMER_SECRET'],
                 os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                 os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

def get_first_tweet(screen_name):
  count = None
  oldest_id = None
  while True:
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
    if count == 1:
      return data[0]
    else:
      oldest_id = data[-1]['id_str']
  
def get_tweet(tweet_id):
  print('Fetching tweet_id: %s' % tweet_id)
  resp = api.request('statuses/oembed', {'id': tweet_id, 'omit_script': 1})
  print(repr(resp.headers))
  return resp.response.json()
