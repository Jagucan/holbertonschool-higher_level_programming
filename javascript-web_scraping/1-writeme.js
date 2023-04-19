#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const textWrithe = process.argv[3];

fs.writeFile(filePath, textWrithe, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
