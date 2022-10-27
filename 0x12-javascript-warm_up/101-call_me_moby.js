#!/usr/bin/node
// executes function some amount of time

exports.callMeMoby = function (x, theFunction) {
  while (x > 0) {
    theFunction();
    x -= 1;
  }
};
