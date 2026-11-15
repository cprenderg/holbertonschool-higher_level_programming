#!/usr/bin/node

const argCount = process.argv.length;

if (argCount === 2) {
  console.log('No argument');
}

if (argCount === 3) {
  console.log('Argument found');
}

if (argCount > 3) {
  console.log('Arguments found');
}
