#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <api_url>');
  process.exit(1);
}

// Get the API URL from the command-line argument
const apiUrl = process.argv[2];

// Perform a GET request to fetch the data from the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    // Parse the JSON response
    const todos = JSON.parse(body);

    // Initialize an object to store the count of completed tasks per user
    const userCompletedTasks = {};

    // Process the tasks
    todos.forEach(todo => {
      if (todo.completed) {
        if (!userCompletedTasks[todo.userId]) {
          userCompletedTasks[todo.userId] = 0;
        }
        userCompletedTasks[todo.userId] += 1;
      }
    });

    // Print the result
    console.log(userCompletedTasks);
  } catch (parseError) {
    console.error(parseError);
  }
});
