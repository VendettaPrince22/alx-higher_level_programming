#!/usr/bin/node
const { argv } = require('node:process');

const myArray = argv.slice(2);
const bigNum = myArray.sort(function (a, b) { return b - a; });

if (argv.length < 4) {
  console.log(0);
} else {
  console.log(bigNum[1]);
}
