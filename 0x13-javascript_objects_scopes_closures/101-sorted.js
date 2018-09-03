#!/usr/bin/node

let dict = require('./101-data.js').dict;
let d = {};

for (var k in dict) {
  if (!(dict[k] in d)) {
    d[dict[k]] = [k];
  } else {
    d[dict[k]].push(k);
  }
}

console.log(d);
