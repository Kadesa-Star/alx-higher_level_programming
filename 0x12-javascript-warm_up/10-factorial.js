#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const args = process.argv.slice(2);
const num = parseInt(args[0], 10);

const result = factorial(num);
console.log(result);
