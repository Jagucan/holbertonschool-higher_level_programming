#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const characterId = 18;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  const wedgeFilms = films.filter((film) => {
    return film.characters.includes(
      'https://swapi-api.hbtn.io/api/people/' + characterId + '/'
    );
  });

  console.log(wedgeFilms.length);
});
