#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  return a + b;
}

const x = parseInt(argv[2]);
const y = parseInt(argv[3]);

console.log(add(x, y));
