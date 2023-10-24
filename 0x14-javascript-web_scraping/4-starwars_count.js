#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const peopleId = '18';

request(url, (error, response, body) => {
  if (!error) {
    const responseJson = JSON.parse(response.body);
    let count = 0;
    let movie;
    let index;
    let chars = [];
    for (movie in responseJson.results) {
      chars = responseJson.results[movie].characters;
      for (index in chars) {
        if (chars[index].includes(peopleId)) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
