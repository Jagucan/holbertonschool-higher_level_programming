#!/usr/bin/node
$(document).ready(function () {
  const url = 'https://stefanbohacek.com/hellosalut/?lang=fr';
  $.getJSON(url, function (data) {
    $('<p>').text(data['hello']).appendTo('DIV#hello');
  });
});
