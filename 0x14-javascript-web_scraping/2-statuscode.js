#!/usr/bin/node

const request = require('request');

const endpoint = process.argv[2];

request.get(endpoint).on('res', function (response) {
  console.log(`code: ${res.statusCode}`);
});
