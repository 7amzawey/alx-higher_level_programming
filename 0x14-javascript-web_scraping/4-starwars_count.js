#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let i = 0; let j = 0; let count = 0;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(`${error.message}`);
    console.log(response);
  }
  const jsonResp = JSON.parse(body);
  if (jsonResp.results[0].characters[0] !== 'https://swapi-api.alx-tools.com/api/people/1/') {
    console.log('nice');
  }
  while (jsonResp.results[i]) {
    while (jsonResp.results[i].characters[j]) {
      if (jsonResp.results[i].characters[j] === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count++;
      }
      j++;
    }
    j = 0;
    i++;
  }
  console.log(count);
});
