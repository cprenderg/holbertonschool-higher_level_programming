#!/usr/bin/node

const arg1 = process.argv[2];
const number1 = Number(arg1);
const arg2 = process.argv[3];
const number2 = Number(arg2);

if (arg1 !== undefined && arg1.trim() !== '' && !Number.isNaN(number1)) {
  if (arg2 !== undefined && arg2.trim() !== '' && !Number.isNaN(number2)) {
    console.log(number1 + number2);
  } else {
    console.log('NaN');
  }
} else {
  console.log('NaN');
}
