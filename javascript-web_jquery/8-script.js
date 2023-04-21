#!/usr/bin/node
$(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.getJSON(url, function (data) {
    for (const title of data.results) {
      $('<li>').text(title.title).appendTo('UL#list_movies');
    }
  });
});
