#!/usr/bin/node
function fact(n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 1 || n === 0) {
    return 1;
  }
  return n * fact(n - 1);
}

console.log(fact(process.argv[2]));
