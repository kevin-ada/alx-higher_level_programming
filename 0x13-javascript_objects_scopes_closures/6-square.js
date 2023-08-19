#!/usr/bin/node

const Squarebase = require('./5-square');

class Square extends Squarebase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; ++i) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;