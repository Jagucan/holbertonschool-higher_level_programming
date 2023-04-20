#!/usr/bin/node
const request = require('request');
const myUrl = process.argv[2];

request.get(myUrl, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
