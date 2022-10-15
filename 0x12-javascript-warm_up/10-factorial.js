#!/usr/bin/node

const n = Number(process.argv[2]);

if (isNaN(n)) {
  console.log('1');
} else {
  console.log(fact(n));
}

function fact (n) {
  if (n <= 1) {
    return 1;
  }
  return n * fact(n - 1);
}
