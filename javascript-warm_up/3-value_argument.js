#!/usr/bin/node

const args = process.argv.slice(2);

if (args[0] === undefined) {
  console.log('not found');
} else {
  console.log(args[0]);
}
