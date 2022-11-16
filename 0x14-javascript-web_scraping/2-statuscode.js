#!/usr/bin/node
// Display the status of a GET request

const request = require('request');
const url = process.argv[2];

request(url, (response) => {
  console.log('code: ' + response.statusCode);
});
