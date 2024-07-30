#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <url>');
  process.exit(1);
}

// Get the URL from the command-line argument
const url = process.argv[2];

// Perform a GET request
request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
