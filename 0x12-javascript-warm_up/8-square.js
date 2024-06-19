#!/usr/bin/node

const args = process.argv.slice(2);
const size = parseInt(args[0], 10);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      let line = '';
      for (let j = 0; j < size; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }
}
