#!/usr/bin/node

const args = process.argv.slice(2);

if (!isNaN(args)) {
  for (let l = 1; l <= args; l++) {
    let square = '';
    for (let w = 1; w <= args; w++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
