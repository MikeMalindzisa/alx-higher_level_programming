#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const endpoint = process.argv[2];
const fileName = process.argv[3];

const fileStream = fs.createWriteStream(fileName);

fileStream.on('error', (err) => {
  console.error(err);
  fileStream.close();
});

request(endpoint)
  .on('error', (err) => {
    console.error(err);
    fileStream.close();
    fs.unlinkSync(fileName);
  })
  .pipe(fileStream)
  .on('finish', () => {
    fileStream.close();
  });
