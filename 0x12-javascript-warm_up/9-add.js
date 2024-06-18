#!/usr/bin/node
args = process.argv.slice(2);
function add(a, b) {
	a = args[0];
	b = args[1];
	console.log(a + b);
}
