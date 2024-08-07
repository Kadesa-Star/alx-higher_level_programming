0x15. JavaScript - Web jQuery
===================================

Why jQuery Makes Front-End Programming Easy:
=============================================

jQuery simplifies DOM manipulation, event handling, and AJAX requests, allowing you to write less code to achieve the same results compared to using plain JavaScript. It abstracts browser inconsistencies and provides a unified API.

Selecting HTML Elements:
=========================

JavaScript: You can use methods like document.querySelector() and document.getElementById() to select elements.
jQuery: You use the $ function, e.g., $('#elementId'), $('.className'), and $('tagName').
Differences Between ID, Class, and Tag Name Selectors:

ID Selector: #myId selects a unique element with the specific ID.
Class Selector: .myClass selects all elements with the specified class.
Tag Selector: tagName selects all elements of that type, e.g., p selects all <p> tags.

Modifying HTML Element Style:
=============================

JavaScript: Use element.style.property = 'value'.
jQuery: Use $(selector).css('property', 'value').

Getting and Updating HTML Element Content:
============================================

JavaScript: Use element.innerHTML to get or set HTML content.
jQuery: Use $(selector).html() to get or $(selector).html('new content') to set HTML content.
Modifying the DOM:
=======================

1. JavaScript: Use methods like appendChild(), removeChild(), and createElement().
2. jQuery: Use methods like .append(), .prepend(), .remove(), and .clone().

Making GET and POST Requests with jQuery AJAX:
===============================================
1. GET Request: $.get('url', callbackFunction).
2. POST Request: $.post('url', data, callbackFunction).
3. Listening/Bonding to DOM Events:

1. JavaScript: Use element.addEventListener('event', function).
2. jQuery: Use $(selector).on('event', function).
