$(document).ready(function() {
  $('.menu').click(() => $('nav').addClass('open-nav'));
  $('.close').click(() => $('nav').removeClass('open-nav'));
});