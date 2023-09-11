#!/usr/bin/node
let i = 0;
let j = 0;
const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  let row = '';
  while (i < arg) {
    while (j < arg) {
	    row += 'X';
	    j++;
    }
    console.log(row);
    i++;
  }
}
