#!/usr/bin/node
// Arguement to show what the user does

const args = process.argv[2];

if (args === undefined) {
  console.log('No argument');
} else {
  console.log(args);
}
