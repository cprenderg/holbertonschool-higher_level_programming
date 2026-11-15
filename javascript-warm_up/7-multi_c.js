#!/usr/bin/node

const arg = process.argv[2];
const userInput = Number(arg);

if (arg !== undefined && arg.trim() !== '' && !Number.isNaN(userInput)) {
  let i = 0;
  while (i < userInput) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
