#!/usr/bin/node
const request = require('request');

async function showHeader () {
  try {
    if (process.argv.length < 3) {
      console.error('Usage: node script.js url');
      process.exit(1);
    }

    const url = process.argv[2];
    const response = await request.get(url);
    console.log('code: ' + response.status);
  } catch (error) {
    console.error('Error during request: ', error);
  }
}

showHeader();
