#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const integer = process.argv;

if ((!isNaN(integer[2])) && (!isNaN(integer[3]))) {
  const sum = add(Number(integer[2]), Number(integer[3]));
  console.log(sum);
} else {
  console.log('NaN');
}
