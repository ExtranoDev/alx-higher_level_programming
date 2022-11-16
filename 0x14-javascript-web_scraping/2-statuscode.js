#!/usr/bin/node
// Display the status of a GET request

const request = require('request');
const url = process.argv[2];

request.get(url, (err, resp) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + resp.statusCode);
  }
});
