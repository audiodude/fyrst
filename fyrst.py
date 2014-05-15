import os
from twython import Twython

api = Twython(os.environ['TWITTER_CONSUMER_KEY'],
              access_token=os.environ['TWITTER_OAUTH2_ACCESS_TOKEN'])


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
    data = api.get_user_timeline(**params)
    count = len(data)
    if count == 1:
      data[0]['html'] = api.get_oembed_tweet(id=data[0]['id_str'])['html']
      return data[0]
    else:
      oldest_id = data[-1]['id_str']

