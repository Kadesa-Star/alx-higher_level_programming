#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <url> <file_path>');
  process.exit(1);
}

// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Perform a GET request to fetch the content of the URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Write the response body to the file
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
