#!/usr/bin/node
// Display the status of a GET request

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
