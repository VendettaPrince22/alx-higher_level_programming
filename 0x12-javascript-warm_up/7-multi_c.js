#!/usr/bin/node
const { argv } = require('node:process');

const myNumber = parseInt(argv[2]);
if (isNaN(myNumber)) {
  console.log('Missing number of occurrences');
}

let i = 0;
while (i < myNumber) {
  console.log('C is fun');
  i++;
}
