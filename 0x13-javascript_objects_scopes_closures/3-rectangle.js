#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      let j = 0;
      let string = '';
      while (j < this.width) {
        string += 'X';
        j++;
      }
      console.log(string);
      i++;
    }
  }
}

module.exports = Rectangle;
