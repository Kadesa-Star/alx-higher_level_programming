# JavaScript Web Scraping

## Project Overview

This project is designed to teach you how to perform web scraping using JavaScript. Web scraping involves extracting data from web pages, and this project will guide you through using JavaScript and Node.js to accomplish this task. You'll work with HTTP request libraries, JSON data, and file operations to scrape and process web data.

## Learning Objectives

By the end of this project, you will:

1. **Understand JavaScript Programming**: Learn why JavaScript is a powerful language for web scraping and other tasks.
2. **Manipulate JSON Data**: Get comfortable with parsing, handling, and formatting JSON data.
3. **Use HTTP Request Libraries**: Master making HTTP requests and handling responses with the `request` module.
4. **Perform File Operations**: Read and write files using the `fs` module in Node.js.

## Web Scraping Details

### What is Web Scraping?

Web scraping is the process of extracting data from websites. It involves sending HTTP requests to web servers, retrieving HTML content, and then parsing this content to extract useful information. JavaScript, along with Node.js, provides tools and libraries that make web scraping straightforward and efficient.

### Key Concepts

1. **HTTP Requests**: Web scraping involves making HTTP requests to retrieve web page content. JavaScript libraries like `request` and `fetch` allow you to make these requests and handle responses.
   
2. **Parsing HTML**: Once you have the HTML content of a web page, you need to parse it to extract the required information. This can be done using libraries such as `cheerio`, which allows you to manipulate HTML content in a jQuery-like way.

3. **Handling JSON**: Data extracted from web pages is often in JSON format. Understanding how to parse and manipulate JSON data is crucial for effectively processing the scraped information.

4. **File Operations**: The `fs` module in Node.js allows you to read from and write to files. This is useful for saving the scraped data to local files for further analysis or processing.

## Requirements

- **Editors**: Use vi, vim, or emacs for editing files.
- **Node.js Version**: Ensure compatibility with Node.js version 14.x on Ubuntu 20.04 LTS.
- **File Formatting**:
  - All files must end with a new line.
  - Each file should start with `#!/usr/bin/node`.
- **Code Style**: Follow the semistandard style guide, including the use of semicolons.
- **Executable Files**: Ensure all scripts are executable.
- **Plagiarism**: All work must be original. Copying or pasting from others is strictly forbidden.

## Setup

1. **Install Node.js 14**:
   ```bash
   curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
   sudo apt-get install -y nodejs
