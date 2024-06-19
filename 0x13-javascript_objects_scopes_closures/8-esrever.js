#!/usr/bin/node

exports.esrever = function (list) {
  const myList = [];
  let i = 0;
  const x = list.length;

  while (i < x) {
    myList.push(list.pop());
    i++;
  }
  return myList;
};
