#!/usr/bin/node
const args = process.argv.slice(2);
const size = parseInt(args[0]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
}
