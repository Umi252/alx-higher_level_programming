#!/usr/bin/node
const fs = require('fs');
const [sourceFile1, sourceFile2, destinationFile] = process.argv.slice(2);
const concatenatedData = fs.readFileSync(sourceFile1, 'utf-8') + fs.readFileSync(sourceFile2, 'utf-8');
fs.writeFileSync(destinationFile, concatenatedData);
console.log(`Files '${sourceFile1}' and '${sourceFile2}' successfully concatenated to '${destinationFile}'.`);
