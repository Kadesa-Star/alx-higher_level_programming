* JAVASCRIPT OBJECTS

javaScript objects and classes are fundamental concepts that are crucial for understanding how to work with structured data and object-oriented programming (OOP) in JavaScript

* JavaScript Objects
What are Objects?
Objects in JavaScript are collections of key-value pairs, where the keys are strings (or symbols) and the values can be any type of data, including other objects. Objects are used to store and organize data in a structured way.

Creating Objects
There are several ways to create objects in JavaScript:
1. Object Literal Syntax:
    onst person = {
          name: "John Doe",
            age: 30,
              isEmployed: true,
                greet: function() {
                        console.log("Hello, my name is " + this.name);
                          }
    };

2. Using the Object Constructor:
    const person = new Object();
    person.name = "John Doe";
    person.age = 30;
    person.isEmployed = true;
    person.greet = function() {
          console.log("Hello, my name is " + this.name);
    };

3. Using Object.create():
    const person = Object.create(null);
    person.name = "John Doe";
    person.age = 30;
    person.isEmployed = true;
    person.greet = function() {
          console.log("Hello, my name is " + this.name);
    };

** Accessing Object Properties
console.log(person.name); // Dot notation
console.log(person["age"]); // Bracket notation

** Modifying Objects
person.job = "Engineer"; // Adding a property
person.age = 31; // Modifying a property
delete person.isEmployed; // Deleting a property

** Iterating over object properties using for loop
for (let key in person) {
      if (person.hasOwnProperty(key)) {
              console.log(key + ": " + person[key]);
                }
}
* JavaScript Classes
What are Classes?
Classes in JavaScript are a blueprint for creating objects with predefined properties and methods. They are introduced in ECMAScript 2015 (ES6) and provide a more formal and convenient way to define object constructors and prototypes.
~                                                                                                                                                                          
