$(document).ready(function () {
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function () {
    $('.my_list li').eq(1).remove();
  });

  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
