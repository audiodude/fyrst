function fetch() {
  $.ajax({
    'type': 'POST',
    'url': '/first_tweet',
    'data': {
      'screen_name': $('#screen-name').val()
    },
    'dataType': 'json',
    'success': on_fetch_success,
    'error': on_fetch_error
  });
  window.console.log('ajax dispatched');
};

function on_fetch_success(data, status, xhr) {
  $('#tweet').text(data.text).show();
}

function on_fetch_error(xhr, errorType, error) {
  $('#error').show();
}
