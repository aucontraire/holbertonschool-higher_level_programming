#!/usr/bin/node

const request = require('request');

const options = {
  url: 'http://swapi.co/api/films/' + process.argv[2],
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const chars = data['characters'];
    let i;
    for (i = 0; i < chars.length; i++) {
      request(chars[i], function (error, response, body) {
        if (!error && response.statusCode === 200 && body) {
          const cdata = JSON.parse(body);
          console.log(cdata['name']);
        }
      });
    }
  }
}

request(options, callback);
