#!/usr/bin/node

const arg = process.argv[2];
const userInput = Number(arg);
let row = '';

if (arg !== undefined && arg.trim() !== '' && !Number.isNaN(userInput)) {
  let i = 0;
  while (i < userInput) {
    row = row + 'X';
    i++;
  }
  i = 0;
  while (i < userInput) {
    console.log(row);
    i++;
  }
} else {
  console.log('Missing size');
}
