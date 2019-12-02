
import { Typed } from './lib'
// Export your custom function for declarative use
export { type, navActivePage, movingBackgroundImage}

// Code your custom function
function type( strings ) {
  var typed = new Typed('#typed', {
    stringsElement: '#typed-strings',
    typeSpeed: 100,
    backSpeed: 20,
    loop: true,
    loopCount: Infinity
  });
}


function navActivePage(){
  $('nav li a[href=".' + location.pathname + '"]').addClass('active');
  if (location.pathname == '/') $('nav li a[href="./index.html"]').addClass('active');
}


function movingBackgroundImage(){
  var bg = document.querySelector('.hero-full-container');
  var windowWidth = window.innerWidth / 5;
  var windowHeight = window.innerHeight / 5 ;

  bg.addEventListener('mousemove', (e) => {
    var mouseX = e.clientX / windowWidth;
    var mouseY = e.clientY / windowHeight;
    
    bg.style.transform = `translate3d(-${mouseX*1.5}px, -${mouseY*1.5}px, 0)`;
  });
}

