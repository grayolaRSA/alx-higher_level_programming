#!/usr/bin/node
const SquareN = require('./5-square');

class Square extends SquareN {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let s = '';
      for (let j = 0; j < this.height; j++) {
        s += c;
      }
      console.log(s);
    }
  }
}
module.exports = Square;
