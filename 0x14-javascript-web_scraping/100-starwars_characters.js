#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const responseJson = JSON.parse(response.body);
    let index;
    let chars = [];
    chars = responseJson.characters;
    for (index in chars) {
      request(chars[index], (err, resp, core) => {
        if (!err) {
          console.log(JSON.parse(resp.body).name);
        }
      });
    }
  }
});
