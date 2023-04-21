#!/usr/bin/node
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.getJSON(url, function (data) {
    const name = data.name;
    $('<p>').text(name).appendTo('div#character');
  });
});
