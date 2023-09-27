#!/usr/bin/node

const request = require('request')

request.get(process.argv[2], (error, response, body) => {
    if (error){
        throw error
    }else {
        console.log(`code: ${response.statusCode}`)
    }
})