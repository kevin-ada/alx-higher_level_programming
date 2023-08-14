#!/usr/bin/node
let num = process.argv[2];

num = parseInt(num);

if (Number.isInteger(num)) {
  console.log('My number: ', num);
} else {
  console.log('Not a number');
}
