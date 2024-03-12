#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.dim1 = w;
      this.dim2 = h;
    }
  }

  print () {
    for (let i = 0; i < this.dim2; i++) {
      let line = '';
      for (let j = 0; j < this.dim1; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    const temp = this.dim1;
    this.dim1 = this.dim2;
    this.dim2 = temp;
  }

  double () {
    this.dim1 *= 2;
    this.dim2 *= 2;
  }
}

module.exports = Rectangle;
