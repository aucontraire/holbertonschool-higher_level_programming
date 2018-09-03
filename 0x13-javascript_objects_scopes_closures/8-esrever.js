#!/usr/bin/node

exports.esrever = function (list) {
  let last = list.length - 1;
  let i;
  let arr = [];
  for (i = last; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};
