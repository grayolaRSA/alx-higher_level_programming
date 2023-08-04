#!/usr/bin/node
const { readFile } = require('fs').promises;
async function readAndPrint () {
  try {
    if (process.argv.length < 3) {
      console.error('Usage: node script.js <filename>');
      process.exit(1);
    }

    const filename = process.argv[2];

    const txt = await readFile(filename, 'utf8');
    console.log(txt);
  } catch (error) {
    console.error('Error reading file: ', error);
  }
}
readAndPrint();
