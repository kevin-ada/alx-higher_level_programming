#!/usr/bin/node

const click = $('DIV#red_header').click(function () {
    $('header').addClass('red')
})

click()