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
    const charUrl = 'https://swapi.co/api/people/18/';
    const movies = data['results'];
    let i = 0;
    let count = 0;
    for (i = 0; i < movies.length; i++) {
      if (movies[i]['characters'].indexOf(charUrl) > -1) {
        count += 1;
      }
    }
    console.log(count);
  }
}

request(options, callback);
