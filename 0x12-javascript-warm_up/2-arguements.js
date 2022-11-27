#!/usr/bin/node

const lgt = process.argv.length;

if (lgt === 2) {
  console.log('No argument');
} else if (lgt === 3) {
  console.log('Argument found');
} else if (lgt >= 3) {
  console.log('Arguments found');
}
