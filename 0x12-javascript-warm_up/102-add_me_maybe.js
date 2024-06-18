#!/usr/bin/node
function addMeMaybe(number, theFunction) {
  number + theFunction(number + 1);
}
module.exports = { addMeMaybe }
