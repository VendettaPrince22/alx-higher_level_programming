#!/usr/bin/node
const { argv } = require('node:process');

function factorial (x) {
  let fact = 1;

  while (x > 0) {
    fact = fact * x;
    x--;
  }

  return fact;
}

const num = parseInt(argv[2]);
console.log(factorial(num));
