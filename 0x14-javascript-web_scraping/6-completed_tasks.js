#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const responseJson = JSON.parse(response.body);
    const completedTask = {};
    let index;
    for (index in responseJson) {
      if (responseJson[index].completed === true) {
        if (completedTask[responseJson[index].userId] === undefined) {
          completedTask[responseJson[index].userId] = 1;
        } else {
          completedTask[responseJson[index].userId] += 1;
        }
      }
    }
    console.log(completedTask);
  }
});
