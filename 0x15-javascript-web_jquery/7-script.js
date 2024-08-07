// Wait until the DOM is fully loaded
$(document).ready(function () {
  // Define the URL to fetch data from
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  // Make an AJAX GET request to the URL
  $.get(url, function (data) {
    // Extract the character name from the data
    const characterName = data.name;

    // Update the content of the <div> with ID "character" with the character name
    $('#character').text(characterName);
  });
});
