#!/usr/bin/node
let times = parseInt(process.argv[2]);
let row = 0;
let column = 0;

if (isNaN(times)) {
  console.log('Missing size');
} else {
  for (row = 0; row < times; row++) {
    let s = '';
    for (column = 0; column < times; column++) {
      s += 'X';
    }
    console.log(s);
  }
}
