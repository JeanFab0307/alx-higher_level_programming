#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  constructor (size) {
    super(size);
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
