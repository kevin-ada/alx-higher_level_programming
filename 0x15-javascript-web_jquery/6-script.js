#!/usr/bin/node

const updateHeader = $('DIV#update_header').click(function () {
    $('header').text( 'New Header!!!')
})

updateHeader()