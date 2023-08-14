#!/usr/bin/node
let args = process.argv.slice(2);
if (args.length < 1) {
	console.log("No argument");
} else if (args.length < 2) {
	console.log("Argument found");
} else {
	console.log('Arguments found');
}
