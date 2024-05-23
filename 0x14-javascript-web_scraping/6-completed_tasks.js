#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const completed = {};
  const tasks = JSON.parse(body);

  tasks.forEach(task => {
    if (task.completed === true) {
      completed[task.userId] = (completed[task.userId] || 0) + 1;
    }
  });

  console.log(completed);
});
