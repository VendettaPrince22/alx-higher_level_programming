#!/usr/bin/node
const { argv } = require('node:process');

const myNumber = parseInt(argv[2]);
if (isNaN(myNumber)) {
  console.log('Missing size');
} else {
  let i = 0;

  while (i < myNumber) {
    let j = 0;
    let string = '';
    while (j < myNumber) {
      string += 'X';
      j++;
    }
    console.log(string);
    i++;
  }
}
