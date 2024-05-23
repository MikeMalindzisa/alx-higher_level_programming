#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(endpoint, async function (err, response, body) {
  if (err) {
    console.log(err);
  }
  for (const characterId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(characterId, function (err, response, body) {
        if (err) {
          reject(err);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
