// Ensure the DOM is fully loaded before running the script
$(document).ready(function () {
  // Attach a click event handler to the button with id 'btn_translate'
  $('#btn_translate').click(function () {
    // Get the value entered in the input field with id 'language_code'
    const languageCode = $('#language_code').val().trim(); // Trim whitespace from the input value
    console.log('Language code entered:', languageCode); // Log the entered language code for debugging

    // Check if the input field is not empty
    if (languageCode) {
      // Make a GET request to the API with the specified language code
      $.ajax({
        url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
        method: 'GET',
        dataType: 'json',
        success: function (data) {
          console.log('Data received:', data); // Log the received data for debugging

          // Check if the 'hello' property exists in the response data
          if (data.hello) {
            // Update the content of the div with id 'hello' with the translated "hello" text
            $('#hello').text(data.hello);
          } else {
            // Handle unexpected API response format
            $('#hello').text('Error: Unexpected API response format.');
          }
        },
        error: function (jqXHR, textStatus, errorThrown) {
          // Handle any errors that occur during the API request
          console.log('Request failed:', textStatus, errorThrown); // Log request failure for debugging
          $('#hello').text('Error: Could not fetch translation.');
        }
      });
    } else {
      // If the input field is empty, prompt the user to enter a language code
      $('#hello').text('Please enter a language code.');
    }
  });
});
