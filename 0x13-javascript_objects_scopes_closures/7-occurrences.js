#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  for (const i of list) {
    if (i === searchElement) { occurence += 1; }
  }
  return occurence;
};
