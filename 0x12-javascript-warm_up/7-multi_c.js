#!/usr/bin/node
const args = process.argv.slice(2);
const num = parseInt(args[0]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
