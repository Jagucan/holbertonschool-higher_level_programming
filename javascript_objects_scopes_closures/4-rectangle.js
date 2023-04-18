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

  print () {
    for (let l = 0; l < this.height; l++) {
      let rectangle = '';
      for (let w = 0; w < this.width; w++) {
        rectangle += 'X';
      }
      console.log(rectangle);
    }
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    const r = this.width;
    this.width = this.height;
    this.height = r;
  }
}

module.exports = Rectangle;
