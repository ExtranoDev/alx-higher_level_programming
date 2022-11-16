#!/usr/bin/node
// Counts number of star war movies Wedge Antilles did

const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request.get(url, (err) => {
  if (err) { console.log(err); }
}).pipe(fs.createWriteStream(process.argv[3]));
