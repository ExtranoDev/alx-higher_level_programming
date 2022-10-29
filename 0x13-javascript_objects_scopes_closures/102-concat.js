#!/usr/bin/node

const { readFileSync, writeFile } = require('fs');
const text1 = readFileSync(process.argv[2], 'utf-8');
const text2 = readFileSync(process.argv[3], 'utf-8');
const data = text1 + text2;

writeFile(process.argv[4], data, (err) => {
  if (err) throw err;
});
