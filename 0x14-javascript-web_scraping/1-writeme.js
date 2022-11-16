#!/usr/bin/node

/*
a script that writes a string to a file
*/

const file = process.argv[2];
const string = process.argv[3];
const fs = require('fs');

fs.writeFile(file, string, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
