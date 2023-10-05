#!/usr/bin/node

$.ajax({
    method:'GET',
    url:'https://swapi-api.alx-tools.com/api/films/?format=json',
    dataType:'JSON',
}).done(function (data){
    $('UL#list_movies').append(`<li>${data}</li>`)
})