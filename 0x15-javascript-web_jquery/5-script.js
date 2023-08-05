$('DIV#add_item').click(function () {
  const newItem = $('<li>New Item</li>');
  newItem.appendTo('UL.my_list');
});
