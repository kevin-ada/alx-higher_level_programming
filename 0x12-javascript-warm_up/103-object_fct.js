#!/usr/bin/node

// function increment obj

const myObject = {
  type: 'object',
  value: 12
};

myObject.incr = function () {
  myObject.value += 1;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
