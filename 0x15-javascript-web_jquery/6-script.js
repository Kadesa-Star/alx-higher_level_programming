// Wait until the DOM is fully loaded
$(document).ready(function () {
  // Set up a click event handler for the <div> with ID "update_header"
  $('#update_header').click(function () {
    // Update the text of the <header> element
    $('header').text('New Header!!!');
  });
});
