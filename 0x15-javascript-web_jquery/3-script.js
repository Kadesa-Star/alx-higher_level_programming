// Wait until the DOM is fully loaded
$(document).ready(function () {
  // Set up a click event handler for the <div> with ID "red_header"
  $('#red_header').click(function () {
    // Add the class 'red' to the <header> element
    $('header').addClass('red');
  });
});
