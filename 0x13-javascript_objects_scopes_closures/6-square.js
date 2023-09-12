#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let i = 0;
    let j = 0;
    let row = '';
    while (i < this.height) {
	    while (j < this.width) {
        row += c;
        j++;
	    }
	    console.log(row);
	    i++;
    }
  }
};
