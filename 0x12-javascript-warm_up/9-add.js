#!/usr/bin/node
let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);

function add(a, b) {
  return a + b;
}

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
