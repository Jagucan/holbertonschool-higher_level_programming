#!/usr/bin/node
$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const newElementAdded = $('<li>Item</li>');
    newElementAdded.appendTo('UL.my_list');
  });
});
