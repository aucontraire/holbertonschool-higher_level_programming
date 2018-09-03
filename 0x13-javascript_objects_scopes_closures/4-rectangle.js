#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let rows, columns;

    for (rows = 0; rows < this.height; rows++) {
      let str = '';
      for (columns = 0; columns < this.width; columns++) {
        str += 'X';
      }
      console.log(str);
    }
  }
  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
