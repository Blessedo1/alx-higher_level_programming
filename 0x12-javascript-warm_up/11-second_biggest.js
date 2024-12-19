#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  let first = Number(args[0]);
  let second = Number(args[1]);

  if (first === second) {
    console.log(0);
  } else {
    for (let i = 0; i < args.length; i++) {
      const current = Number(args[i]);
      if (current > first) {
        second = first;
        first = current;
      } else if (current > second && current < first) {
        second = current;
      }
    }
    console.log(second);
  }
}
