#!/usr/bin/node
const { writeFile } = require('fs').promises;
async function writeAndPrint () {
  try {
    if (process.argv.length < 4) {
      console.error('Usage: node script.js <filename> text');
      process.exit(1);
    }

    const filename = process.argv[2];
    const filetext = process.argv[3];
    await writeFile(filename, filetext, 'utf8');
  } catch (error) {
    console.error('Error writing to file: ', error);
  }
}
writeAndPrint();
