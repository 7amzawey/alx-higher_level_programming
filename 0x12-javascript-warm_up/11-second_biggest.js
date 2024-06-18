#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0]) || isNaN(args[1])) {
  console.log(0);
} else {
  for (let i = 1; i < args.length; i++) {
    let j = i;
    while (args[j - 1] > args[j] && j > 0) {
      const temp = args[j - 1];
      args[j - 1] = args[j];
      args[j] = temp;
      j--;
    }
  }
  console.log(args[args.length - 2]);
}
