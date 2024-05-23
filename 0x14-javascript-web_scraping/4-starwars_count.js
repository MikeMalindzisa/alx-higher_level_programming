#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  let count = 0;
  const data = JSON.parse(body);
  for (const result of data.results) {
    if (result.characters.some(url => url.includes('18'))) {
      count++;
    }
  }

  console.log(count);
});
