#!/usr/bin/node
const args = process.argv.slice(2);

if (args[0] is not int) {
  console.log('Not a number');
} else {
  console.log('My number: ' + args[0]);
}
