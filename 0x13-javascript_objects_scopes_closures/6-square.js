#!/usr/bin/node

const SquareBase = require('./5-square');

module.exports = class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let temp = this.width;
    while (temp > 0) {
      console.log(c.repeat(this.width));
      temp -= 1;
    }
  }
};
