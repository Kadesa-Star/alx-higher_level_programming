// 103-script.js

// Function to fetch and display the translation
function fetchTranslation () {
  // Get the language code from the input field
  const langCode = $('#language_code').val();

  // Check if the language code is not empty
  if (langCode.trim() !== '') {
    // Perform the AJAX request to fetch the translation
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      type: 'GET',
      data: { lang: langCode },
      success: function (response) {
        // Update the content of the DIV#hello with the translated greeting
        $('#hello').text(response.hello);
      },
      error: function () {
        // Handle any errors during the request
        $('#hello').text('Could not fetch translation.');
      }
    });
  } else {
    // Handle the case where the language code is empty
    $('#hello').text('Please enter a language code.');
  }
}

// Event handler for the Translate button click
$('#btn_translate').click(fetchTranslation);

// Event handler for Enter key press in the input field
$('#language_code').keypress(function (event) {
  // Check if the Enter key (key code 13) is pressed
  if (event.which === 13) {
    fetchTranslation();
  }
});
