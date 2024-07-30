#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <api_url>');
  process.exit(1);
}

// Get the API URL from the command-line argument
const apiUrl = process.argv[2];

// Define the character ID for Wedge Antilles
const wedgeAntillesId = 18;

// Perform a GET request to fetch the movies data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body
  const data = JSON.parse(body);

  // Initialize a counter for movies with Wedge Antilles
  let count = 0;

  // Iterate through the results and check for Wedge Antilles
  data.results.forEach(movie => {
    if (movie.characters.some(character => character.includes(wedgeAntillesId))) {
      count++;
    }
  });

  // Print the number of movies
  console.log(count);
});
