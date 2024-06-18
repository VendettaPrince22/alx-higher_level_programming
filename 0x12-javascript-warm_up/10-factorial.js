#!/usr/bin/node
const { argv } = require('node:process');

function factorial (x) {
  if (x === 0 || x === 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
