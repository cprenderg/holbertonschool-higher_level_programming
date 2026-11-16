#!/usr/bin/node

const arg1 = process.argv[2];
const number1 = Number(arg1);

if (arg1 !== undefined && arg1.trim() !== '' && !Number.isNaN(number1)) {
  console.log(factorial(number1));
} else {
  console.log('1');
}

function factorial (number) {
  if (number === 1) {
    return 1;
  }
  return number * factorial(number - 1);
}
