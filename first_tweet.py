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
    print('Fetching next batch...')
    resp = api.request('statuses/user_timeline', params)
    data = resp.response.json()
    count = len(data)
    if count:
      oldest_id = int(data[-1]['id']) - 1
      potential_first_tweet = data[-1]

  return potential_first_tweet


if __name__ == '__main__':
  print(get_first_tweet('audiodude'))
  
