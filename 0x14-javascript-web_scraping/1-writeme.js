#!/usr/bin/node

const fs = require('fs')

const file  = process.argv[2]


fs.writeFile(file, 'Python is cool', (err) => {
    if (err){
        throw err
    }
    else {
        console.log("Complete")
    }
})