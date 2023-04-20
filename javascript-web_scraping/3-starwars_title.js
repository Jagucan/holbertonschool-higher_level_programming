#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

request.get(
  'https://swapi-api.hbtn.io/api/films/' + id,
  function (error, response, body) {
    if (error) {
      console.log(error);
    }
    if (response.statusCode !== 200) {
      console.log(error);
    }
    const data = JSON.parse(body);
    console.log(data.title);
  }
);
