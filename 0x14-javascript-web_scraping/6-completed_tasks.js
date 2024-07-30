#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
data = {};
request.get(url, (error, response, body) => {
    if (error) {
        console.log(error);
    }
    const users = JSON.parse(body);
    let i = 0;
    console.log(users[9].userId);
    while(users[i]) {
        if (users[i].userId !== users[i++].userId) {
            data[`${users[i].userId}`] = null; 
        };
        i++;
    };
    console.log(data);
});