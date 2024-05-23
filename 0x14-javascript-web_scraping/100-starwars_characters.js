#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

// Function to fetch character name from character URL
function getCharacterName (characterId) {
  return new Promise((resolve, reject) => {
    request(characterId, function (err, response, body) {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  const characters = JSON.parse(body).characters;
  const characterPromises = characters.map(getCharacterName);

  Promise.all(characterPromises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(err => {
      console.error(err);
    });
});
