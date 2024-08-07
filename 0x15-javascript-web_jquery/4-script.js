// Wait until the DOM is fully loaded
$(document).ready(function () {
  // Set up a click event handler for the <div> with ID "toggle_header"
  $('#toggle_header').click(function () {
    // Check if the <header> currently has the class 'red'
    if ($('header').hasClass('red')) {
      // If it does, remove 'red' and add 'green'
      $('header').removeClass('red').addClass('green');
    } else {
      // Otherwise, remove 'green' and add 'red'
      $('header').removeClass('green').addClass('red');
    }
  });
});
