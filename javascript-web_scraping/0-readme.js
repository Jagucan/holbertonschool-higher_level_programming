#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2]; // Get the file path from the command line arguments

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
