#!/usr/bin/node
let i = 0;
const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  while (i < arg) {
    console.log('C is fun');
    i++;
  }
}
