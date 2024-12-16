#!/usr/bin/node
const times = process.argv;

if (times[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < times[2]; i++) {
    console.log('C is fun');
  }
}
