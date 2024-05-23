#!/usr/bin/node

const request = require('request-promise-native');
const filmId = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

async function getCharacterName (characterId) {
  const body = await request(characterId);
  return JSON.parse(body).name;
}

(async () => {
  try {
    const body = await request(endpoint);
    const characters = JSON.parse(body).characters;
    for (const characterId of characters) {
      const name = await getCharacterName(characterId);
      console.log(name);
    }
  } catch (err) {
    console.error(err);
  }
})();
