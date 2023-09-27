#!/usr/bin/node

const request = require('request')
const fs = require('fs')

const url = process.argv[2]

request.get(url, (error, response) =>{
    if (error){
        throw error
    }else {
        fs.writeFile(process.argv[3], `${response.body}`, 'utf-8' ,(err) =>{
            if (err){
                throw error
            }
            }
        )
    }
})