#!/usr/bin/node
let num = parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}
