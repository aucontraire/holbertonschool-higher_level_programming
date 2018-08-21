#!/usr/bin/node
function fact (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 1) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}
console.log(fact(parseInt(process.argv[2])));
