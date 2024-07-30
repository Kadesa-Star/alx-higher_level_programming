#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Get the Movie ID from the command-line argument
const movieId = process.argv[2];

// API URL for the Star Wars movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Fetch the movie data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    // Parse the JSON response
    const movie = JSON.parse(body);

    // Check if the movie has characters
    if (!movie.characters || movie.characters.length === 0) {
      console.log('No characters found for this movie.');
      return;
    }

    // Create an array to hold character URLs
    const characterUrls = movie.characters;

    // Function to fetch character data
    const fetchCharacterData = (url, callback) => {
      request(url, (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        }

        try {
          const character = JSON.parse(body);
          callback(character.name);
        } catch (parseError) {
          console.error(parseError);
        }
      });
    };

    // Function to process all characters
    const processCharacters = (urls) => {
      let count = 0;

      urls.forEach((url) => {
        fetchCharacterData(url, (name) => {
          console.log(name);
          count += 1;
          // If all characters have been processed, exit the process
          if (count === urls.length) {
            process.exit(0);
          }
        });
      });
    };

    // Process all character URLs
    processCharacters(characterUrls);
  } catch (parseError) {
    console.error(parseError);
  }
});
