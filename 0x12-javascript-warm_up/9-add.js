#!/usr/bin/node
console.log(add(Number(process.argv[2]), Number(process.argv[3])));

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  } else {
    return a + b;
  }
}
