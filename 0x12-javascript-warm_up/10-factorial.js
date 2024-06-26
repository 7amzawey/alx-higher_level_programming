#!/usr/bin/node
const args = process.argv.slice(2);
const factor = parseInt(args[0]);

function factorial (n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n === 0 || n === 1) {
    return (1);
  } else {
    return n * (factorial(n - 1));
  }
}
console.log(factorial(factor));
