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
}

module.exports = Rectangle;
