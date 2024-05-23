#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(endpoint, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
