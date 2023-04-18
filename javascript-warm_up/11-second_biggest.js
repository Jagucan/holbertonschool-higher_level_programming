#!/usr/bin/node

const args = process.argv.slice(2);

function findSecondBiggest (args) {
  const num = args.map(Number);
  const sortedArgs = num.sort((a, b) => b - a);

  if (sortedArgs.length < 2) {
    console.log(0);
  } else {
    console.log(sortedArgs[1]);
  }
}

findSecondBiggest(args);
