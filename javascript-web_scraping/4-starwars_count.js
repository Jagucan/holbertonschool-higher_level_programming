#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const urlPeople = 'https://swapi-api.hbtn.io/api/people/';
const characterId = 18;
let count = 0;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  }

  const data = JSON.parse(body);
  const films = data.results;
  for (const film of films) {
    const characters = film.characters;
    if (characters.includes(urlPeople + characterId + '/')) {
      count++;
    }
  }
  console.log(count);
  count = 0;
});
