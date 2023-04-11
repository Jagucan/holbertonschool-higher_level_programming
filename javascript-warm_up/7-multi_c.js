#!/usr/bin/node

const args = process.argv.slice(2);

if (!isNaN(args)) {
  for (let line = 0; line < args[0]; line++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
