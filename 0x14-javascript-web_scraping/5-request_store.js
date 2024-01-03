#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const filepath = process.argv[3];
const url = process.argv[2];

require(url, (err, res, body) => {
  if (err) console.error(err);
  fs.writeFile(filepath, body, {
    if (err) console.error(err);
  });
});
