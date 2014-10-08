var main = function(){
$('.icon-menu').hover(function(){
$('.hidemenu').animate({left:"0px"},200);
});
};



var currentBackground = 0;
var backgrounds = [];
backgrounds[0] = '/static/Black-Guitar-Facebook-Timeline-Cover.png';
backgrounds[1] = '/static/background_wall.jpg';
backgrounds[2] = '/static/Guitar-Strings.jpg';
backgrounds[3] = '/static/playing-guitar.jpg';

function changeBackground() {

    currentBackground++;
    if(currentBackground > 3) currentBackground = 0;

          $('.jumbotron').css({
            'background-image' : "url('" + backgrounds[currentBackground] + "')"
        });
  setTimeout(changeBackground, 3000);
            };


$(document).ready(main);