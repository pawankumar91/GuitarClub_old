
var main = function(){
$('.icon-menu').click(function(){
$('.menu_m').animate({left:"0px"},200);

$('.menu_bar').animate({left: "285px"}, 200);
});
$('.icon-close').click(function(){
$('.menu_m').animate({left:"-400px"},200);
});

};


$(document).ready(main);