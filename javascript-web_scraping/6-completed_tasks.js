#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

const completedTasks = {};

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  for (const task of data) {
    if (task.completed) {
      const userId = task.userId;
      if (!completedTasks[userId]) {
        completedTasks[userId] = 0;
      }
      completedTasks[userId]++;
    }
  }
  console.log(completedTasks);
});
