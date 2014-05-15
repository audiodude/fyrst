function fetch() {
  $.ajax({
    'type': 'POST',
    'url': '/first_tweet',
    'data': {
      'screen_name': $('#screen-name').val()
    },
    'dataType': 'json',
    'beforeSend': function() {
			$('#tweet').text('');
      $('#error').hide();
      $('#loading').show();
    },
    'success': on_fetch_success,
    'error': on_error,
  });
};

function load_tweet(tweet_id) {
  $.ajax({
    'type': 'POST',
    'url': '/tweet',
    'data': {
      'tweet_id': tweet_id
    },
    'dataType': 'json',    
    'success': on_load_tweet_success,
    'error': on_error,
    'complete': function() {
      $('#loading').hide();
    }
  });
}


function on_fetch_success(data, status, xhr) {
  load_tweet(data.id);
}

function on_load_tweet_success(data, status, xhr) {
  window.console.log(data);
  result = $(data.html);

  $('#tweet').html(result);
  result.find('script').appendTo('#tweet');
  $('#tweet').show();
}

function on_error(xhr, errorType, error) {
  $('#error').show();
}
