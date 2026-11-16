#!/usr/bin/node

function add (arg1, arg2) {
  const number1 = Number(arg1);
  const number2 = Number(arg2);

  return number1 + number2;
}

exports.add = add;
