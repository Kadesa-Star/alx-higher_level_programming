// Wait until the DOM is fully loaded
$(document).ready(function () {
  // Add a new <li> element to the list when #add_item is clicked
  $('#add_item').click(function () {
    // Append a new <li> with the text "Item" to the UL with class .my_list
    $('.my_list').append('<li>Item</li>');
  });

  // Remove the last <li> element from the list when #remove_item is clicked
  $('#remove_item').click(function () {
    // Remove the last <li> element from the UL with class .my_list
    $('.my_list li:last-child').remove();
  });

  // Clear all <li> elements from the list when #clear_list is clicked
  $('#clear_list').click(function () {
    // Empty all <li> elements from the UL with class .my_list
    $('.my_list').empty();
  });
});
