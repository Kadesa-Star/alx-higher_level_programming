#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    let result = '';

    function convert (number, base) {
      const hexChars = '0123456789abcdef';
      if (number >= base) {
        convert(Math.floor(number / base), base);
      }
      result += hexChars[number % base];
    }

    convert(number, base);
    return result;
  };
};
