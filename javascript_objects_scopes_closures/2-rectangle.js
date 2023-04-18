#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!isNaN(w) || !isNaN(h)) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      } else {
        return null;
      }
    }
  }
}
module.exports = Rectangle;
