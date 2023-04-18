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
    for (let l = 0; l < this.height * 2; l++) {
      let rectangle = '';
      for (let w = 0; w < this.width * 2; w++) {
        rectangle += 'X';
      }
      console.log(rectangle);
    }
  }

  rotate () {
    for (let l = 0; l < this.width; l++) {
      let rectangle = '';
      for (let w = 0; w < this.height; w++) {
        rectangle += 'X';
      }
      console.log(rectangle);
    }
  }
}

module.exports = Rectangle;
