#!/usr/bin/node
const factorial = n => isNaN(n) || n === 0 ? 1 : n * factorial(n - 1);
const [arg1] = process.argv.slice(2);
const num = parseInt(arg1);
console.log(factorial(num));
