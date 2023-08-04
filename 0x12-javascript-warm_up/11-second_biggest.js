#!/usr/bin/node

let bigNum = 0;
let n;
const arrayNumbers = [];

for (n = 2; n < process.argv.length; n++) {
  if (Number.isNaN(parseInt(process.argv[n])) === false) {
    arrayNumbers[n - 2] = parseInt(process.argv[n]);
  }
}

if (arrayNumbers.length > 1) {
  bigNum = Math.max.apply(null, arrayNumbers);
  n = arrayNumbers.indexOf(bigNum);
  arrayNumbers[n] = -Infinity;
  bigNum = Math.max.apply(null, arrayNumbers);
}

console.log(bigNum);
