#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const films = JSON.parse(body).results;
  const wedgeAntillesId = '18';
  let count = 0;

  films.forEach(film => {
    film.characters.forEach(characterUrl => {
      if (characterUrl.includes(wedgeAntillesId)) {
        count++;
      }
    });
  });

  console.log(count);
});
