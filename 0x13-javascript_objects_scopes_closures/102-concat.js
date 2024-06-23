#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1 = process.argv[2];
const file2 = process.argv[3];
const destination = process.argv[4];

// Function to concatenate two files into a destination file
function concatenateFiles (file1, file2, destination) {
  // Read the content of file1
  fs.readFile(file1, 'utf8', (err, data1) => {
    if (err) {
      console.error(err);
    } else {
      // Read the content of file2
      fs.readFile(file2, 'utf8', (err, data2) => {
        if (err) {
          console.error(err);
        } else {
          // Concatenate contents of file1 and file2
          const concatenatedContent = data1 + data2;
          // Write concatenated content to destination file
          fs.writeFile(destination, concatenatedContent, 'utf8', (err) => {
            if (err) {
              console.error(err);
            }
          });
        }
      });
    }
  });
}

// Call function to concatenate files
concatenateFiles(file1, file2, destination);
