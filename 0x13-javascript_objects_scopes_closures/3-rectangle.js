#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let h = this.height;
    while (h > 0) {
      console.log('X'.repeat(this.width));
      h -= 1;
    }
  }
};
