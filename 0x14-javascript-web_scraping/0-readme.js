#!/usr/bin/node


const fs = require('fs')


fs.readFile(process.argv[1], 'utf8', (err, data) => {
    if (err){
        throw err
    }else {
        console.log(data)
    }
})