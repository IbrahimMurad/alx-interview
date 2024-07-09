#!/usr/bin/node
const request = require('request');
const film_url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request(url, async (error1, response1, body1) => {
  for (character of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(character, (error2, response2, body2) => {
        console.log(JSON.parse(body2).name);
      })
    })
  }
});