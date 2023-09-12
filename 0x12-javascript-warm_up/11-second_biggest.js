#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  console.log(secondBiggest(args));
}

function secondBiggest (arr) {
  let len = arr.length;
  let j;
  let tmp;
  for (let i = 0; i < 2; i++) {
    j = 2;
    while (j < len - 1) {
	    if (arr[j] > arr[j + 1]) {
        tmp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = tmp;
	    }
	    j++;
    }
    len -= 1;
  }
  return arr[j];
}
