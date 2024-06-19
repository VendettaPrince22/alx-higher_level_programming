#!/usr/bin/node
const myList = [];
exports.logMe = function (item) {
  myList.push(item);
  const count = myList.length - 1;
  console.log(count + ':', item);
};
