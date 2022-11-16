#!/usr/bin/node
// write some content to a file

const fs = require('fs');
const msg = process.argv[3];
const filename = process.argv[2];

fs.writeFile(filename, msg, 'utf-8', (err) => {
  if (err) { console.log(err); }
});
