#!/usr/bin/node
const { argv } = require('process');
let out = [];
argv.forEach((val, index) => {
  if (`${index}` === '2') {
    out = val;
  } else if (`${index}` < 2) {
    out = 'No argument';
  }
});
console.log(out);
