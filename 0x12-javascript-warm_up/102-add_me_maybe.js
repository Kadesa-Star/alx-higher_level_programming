#!/usr/bin/node

function incrementAndCall (number, theFunction) {
  number++;
  theFunction(number);
}
module.exports = { incrementAndCall };
