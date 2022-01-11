function headerscroll(){
  var st = $(window).scrollTop();
  if (st > 75) {
    $("header").addClass('new_header')
  } else {
    $("header").removeClass('new_header')
  }

}

$('body').bind('touchmove',headerscroll);
$(window).scroll(headerscroll);
