#!/usr/bin/node

const arg = process.argv[2];
const userInput = Number(arg);

if (arg !== undefined && arg.trim() !== '' && !Number.isNaN(userInput)) {
  console.log('My number: ' + parseInt(userInput));
} else {
  console.log('Not a number');
}
