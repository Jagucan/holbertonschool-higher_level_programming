#!/usr/bin/node

const args = process.argv.slice(2);

if (!isNaN(args)) {
  for (let l = 1; l <= args; l++) {
    let quare = '';
    for (let c = 1; c <= args; c++) {
      quare += '*';
    }
    console.log(e);
  }
} else {
  console.log('Missing size');
}
