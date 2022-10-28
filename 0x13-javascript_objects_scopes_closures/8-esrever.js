#!/usr/bin/node

exports.esrever = function (list) {
  if (list === []) { return []; }
  let arrLength = list.length - 1;
  const newList = [];
  while (arrLength >= 0) {
    newList.push(list[arrLength]);
    arrLength -= 1;
  }
  return newList;
};
