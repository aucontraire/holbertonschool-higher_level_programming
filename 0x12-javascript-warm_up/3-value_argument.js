#!/usr/bin/node
let no_args = true;
process.argv.forEach((val, index) => {
  if (index === 2) {
    console.log(`${val}`);
    no_args = false;
  }
});

if (no_args) {
  console.log('No argument');
}
