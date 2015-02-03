var currentBackground = 0;
var backgrounds = [];
backgrounds[0] = '/static/Black-Guitar-Facebook-Timeline-Cover.png';
backgrounds[1] = '/static/acoustic-guitar-wallpaper-high-resolution-7718[1].jpg';
backgrounds[2] = '/static/Guitar-Strings.jpg';
backgrounds[3] = '/static/playing-guitar.jpg';

function changeBackground() {

    currentBackground++;
    if(currentBackground > 3) currentBackground = 0;

          $('.jumbotron').css({
            'background-image' : "url('" + backgrounds[currentBackground] + "')"
        });
  setTimeout(changeBackground, 4000);

            };

