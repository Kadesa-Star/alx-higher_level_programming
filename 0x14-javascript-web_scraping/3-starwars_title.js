#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

// Get the movie ID from the command-line argument
const movieId = process.argv[2];

// Define the URL for the API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Perform a GET request to fetch the movie details
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body
  const data = JSON.parse(body);

  // Print the title of the movie
  console.log(data.title);
});
