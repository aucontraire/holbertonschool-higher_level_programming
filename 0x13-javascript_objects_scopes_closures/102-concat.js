#!/usr/bin/node

const fs = require('fs');

const fileA = fs.readFileSync(process.argv[2]);
const fileB = fs.readFileSync(process.argv[3]);
const arr = [fileA, fileB];
var file = fs.createWriteStream(process.argv[4]);
arr.forEach(function (line) {
  file.write(line + '\n');
});
