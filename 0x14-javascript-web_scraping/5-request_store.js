#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const apiUrl = process.argv[2];
const file = process.argv[3];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
