#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c !== undefined) {
      let i = 0;
      while (i < this.height) {
        let j = 0;
        let string = '';
        while (j < this.width) {
          string += c;
          j++;
        }
        console.log(string);
        i++;
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
