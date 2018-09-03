#!/usr/bin/node

let dict = require('./101-data').dict;
let d = {};

for (let k in dict) {
  if (!(dict[k] in d)) {
    d[dict[k]] = [k];
  } else {
    d[dict[k]].push(k);
  }
}

console.log(d);
