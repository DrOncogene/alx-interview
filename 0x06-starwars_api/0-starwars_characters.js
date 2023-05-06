#!/usr/bin/env node

const request = require('request');
const util = require('node:util');

const MOVIE_ID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${MOVIE_ID}`;

const get = util.promisify(request.get);

request.get(URL, async (err, res1, body) => {
  if (err) {
    return;
  }
  const characters = await JSON.parse(body).characters;
  await printCharacters(characters);
});

async function printCharacters (characters) {
  for (const charUri of characters) {
    const character = await get(charUri)
      .then(res => JSON.parse(res.body));

    console.log(character.name);
  }
}
