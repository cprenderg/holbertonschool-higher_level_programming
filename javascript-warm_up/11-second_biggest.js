#!/usr/bin/node

const arg1 = process.argv[2];
const number1 = Number(arg1);
const argCount = process.argv.length - 2;
let max = 0;
let second = 0;

if (argCount === 1) {
  console.log('0');
  return;
}

if (arg1 !== undefined && arg1.trim() !== '' && !Number.isNaN(number1)) {
  let i = 2;
  while (i < argCount + 2) {
    if (Number(process.argv[i]) > max) {
      second = max;
      max = Number(process.argv[i]);
    } else if (Number(process.argv[i] < max && Number(process.argv[i] > second))) {
      second = Number(process.argv[i]);
    }
    i++;
  }
}

console.log(second);
