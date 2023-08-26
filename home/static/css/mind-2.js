document.querySelector('#btn').onclick = function() {
    document.querySelector('#slider').classList.toggle("slide-1") ;
    document.querySelector('body').classList.toggle("body-1") ;

}
document.querySelector('#close').onclick = function() {
    document.querySelector('#slider').classList.toggle("slide-1") ;
    document.querySelector('body').classList.toggle("body-1") ;
}

window.onscroll = function() {
    if (window.scrollY >= 300){
        document.querySelector('#container2').style.transform= 'translateX(0) translateY(-100px)'
    }

}

