#!/usr/bin/node

const request = require('request');

const options = {
  url: process.argv[2],
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    let results = {};
    let i = 0;
    for (i = 0; i < data.length; i++) {
      if (!(data[i]['userId'] in results) && data[i]['completed']) {
        results[data[i]['userId']] = 0;
      }
      if (data[i]['completed']) {
        results[data[i]['userId']] += 1;
      }
    }
    console.log(results);
  }
}

request(options, callback);
