#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(`${error.message}`);
    return;
  }

  const characters = JSON.parse(body).characters;
  const names = [];
  let completedRequests = 0;

  characters.forEach((characterUrl, index) => {
    request.get(characterUrl, (err, resp, bd) => {
      if (err) {
        console.log(err);
        completedRequests++;
        if (completedRequests === characters.length) {
          names.forEach(name => console.log(name));
        }
        return;
      }

      const name = JSON.parse(bd).name;
      names[index] = name; // Ensure order
      completedRequests++;
      if (completedRequests === characters.length) {
        names.forEach(name => console.log(name));
      }
    });
  });
});
