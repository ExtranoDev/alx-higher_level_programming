#!/usr/bin/node
// increments and call function

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
