#!/usr/bin/node

const args = process.argv.slice(2);

const numbers = args.map(arg => parseInt(arg, 10));
if (numbers.length <= 1) {
  console.log(0);
} else {
  const sortedUniqueNumbers = Array.from(new Set(numbers)).sort((a, b) => b - a);
  if (sortedUniqueNumbers.length > 1) {
    console.log(sortedUniqueNumbers[1]);
  } else {
    console.log(0);
  }
}
