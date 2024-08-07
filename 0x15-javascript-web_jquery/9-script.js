// Wait until the DOM is fully loaded
$(document).ready(function () {
  // Define the URL to fetch data from
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Make an AJAX GET request to the URL
  $.get(url, function (data) {
    // Extract the value of "hello" from the data
    const helloText = data.hello;

    // Update the content of the <div> with ID "hello"
    $('#hello').text(helloText);
  });
});
