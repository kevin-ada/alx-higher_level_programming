#!/usr/bin/node

const fs = require('fs')

const file  = process.argv[2]


fs.writeFile(file, process.argv[3], (err) => {
    if (err){
        throw err
    }
    else {
        console.log("Complete")
    }
})