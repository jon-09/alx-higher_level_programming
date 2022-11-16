#!/usr/bin/node

/*
a script that display the status code of a GET request.
*/

const url = process.argv[2];
const req = require('request');

req.get(url, (err, res) => {
  if (err) {
    console.error(err);
  }
  console.log('code: ' + res.statusCode);
});
