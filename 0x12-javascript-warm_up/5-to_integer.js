#!/usr/bin/node
const { argv } = require('node:process');

const myNumber = parseInt(argv[2]);
if (isNaN(myNumber)) {
  console.log('Not a number');
} else {
  console.log('My number:', myNumber);
}
