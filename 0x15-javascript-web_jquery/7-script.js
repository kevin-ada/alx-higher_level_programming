#!/usr/bin/node

// JavaScript script that fetches the character

const characterUri = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const $characterDiv = $('div#character');

$.ajax({
    url: characterUri,
    dataType: 'json'
}).done(function (data) {
    $($characterDiv).text(data)
})