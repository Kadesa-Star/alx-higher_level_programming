// Wait until the DOM is fully loaded
$(document).ready(function () {
  // Define the URL to fetch data from
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  // Make an AJAX GET request to the URL
  $.get(url, function (data) {
    // Extract the list of movies from the data
    const movies = data.results;

    // Iterate over each movie
    movies.forEach(function (movie) {
      // Create a new <li> element with the movie title
      const listItem = $('<li>').text(movie.title);

      // Append the <li> element to the <ul> with ID "list_movies"
      $('#list_movies').append(listItem);
    });
  });
});
