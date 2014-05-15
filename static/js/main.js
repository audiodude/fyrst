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
    'complete': function() {
      $('#loading').hide();
    },
    'success': on_fetch_success,
    'error': on_error,
  });
};

function on_fetch_success(data, status, xhr) {
  $('#tweet').html(data.html).show();
  twttr.widgets.load();
}

function on_error(xhr, errorType, error) {
  $('#error').show();
}
