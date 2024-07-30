#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(`${error.message}`);
  }
  const characters = JSON.parse(body).characters;
  characters.forEach(characterUrl => {
    request.get(characterUrl, (err, resp, bd) => {
      if (err) {
        console.log(err);
      }
      const nm = JSON.parse(bd).name;
      console.log(nm);
    });
  });
});
