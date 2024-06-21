#!/usr/bin/node
const list = require('./100-data.js').list;
const myList = list.map((item, index) => item * index);
console.log(list);
console.log(myList);
