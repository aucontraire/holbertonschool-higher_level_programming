#!/usr/bin/node

const fs = require('fs');

const fileA = fs.readFileSync(process.argv[2]);
const fileB = fs.readFileSync(process.argv[3]);
const arr = [fileA, fileB];

for (let i in arr) {
  fs.appendFile('fileC', arr[i] + '\n', (err) => {
    if (err) {
      console.log(err);
    }
  });
}
