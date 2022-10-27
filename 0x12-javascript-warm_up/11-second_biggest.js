#!/usr/bin/node
// scripts searches the second biggest integer in list of args

const numList = process.argv;
numList.shift();
numList.shift();
const lenList = numList.length;

if (lenList <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < lenList; i++) {
    numList[i] = Number(numList[i]);
  } // converts number to integer
  console.log(numList.sort((a, b) => b - a)[1]);
}
