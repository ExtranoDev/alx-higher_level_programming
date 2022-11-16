#!/usr/bin/node
// read text from a file

const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, 'utf-8', function (err, msg) {
  if (err) {
    console.log(err);
  } else {
    console.log(msg);
  }
});
