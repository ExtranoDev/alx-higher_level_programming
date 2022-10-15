#!/usr/bin/node

let fArg = process.argv[2];
let sArg = process.argv[3];

if (fArg === undefined || sArg === undefined) {
  console.log('NaN');
} else {
  fArg = Number(fArg);
  sArg = Number(sArg);
  if (!(isNaN(sArg) || isNaN(fArg))) {
    console.log(add(fArg, sArg));
  } else {
    console.log('NaN');
  }
}

function add (a, b) {
  return a + b;
}
