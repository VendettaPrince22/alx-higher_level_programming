#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  const valueX = list.filter(function (value) { return value === searchElement; });
  return valueX.length;
};
