#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request(url, async function (error, response, body) {
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    const name = await new Promise((resolve) => {
      request(character, function (error, response, body) {
        resolve(JSON.parse(body).name);
      });
    });
    console.log(name);
  }
}
);
