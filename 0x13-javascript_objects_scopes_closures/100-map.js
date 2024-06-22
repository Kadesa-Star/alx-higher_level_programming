#!/usr/bin/node

const { list } = require('./100-data');

// compute new array using map
const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
