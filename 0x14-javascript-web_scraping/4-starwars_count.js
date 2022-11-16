#!/usr/bin/node
// Counts number of star war movies Wedge Antilles did

const request = require('request');
const url = process.argv[2];

request.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    let chrCount = 0;
    for (let i = 0; i < 7; i++) {
      const chars = json.results[i].characters;
      if (chars.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        chrCount++;
      }
    }
    console.log(chrCount);
  }
});
