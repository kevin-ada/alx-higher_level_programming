#!/usr/bin/node

const click = $('DIV#toggle_header').click(function () {
    $('header').toggleClass('red green')
});