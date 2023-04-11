#!/usr/bin/node

const args = process.argv.slice(2);

if (!isNaN(args)) {
  const num = parseInt(args);
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
