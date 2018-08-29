#!/usr/bin/node

if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  let fmax = parseInt(process.argv[2]);
  let nmax = parseInt(process.argv[3]);
  process.argv.forEach((val, index) => {
    if (index > 1) {
      if (fmax < parseInt(val)) {
        nmax = fmax;
        fmax = parseInt(val);
      } else if (parseInt(val) < fmax && parseInt(val) >= nmax) {
        nmax = parseInt(val);
      }
    }
  });
  console.log(nmax);
}
