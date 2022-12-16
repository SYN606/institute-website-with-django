const lightbox = document.getElementById("lightbox");
const btnClose = document.getElementById("btnClose");
let content = document.getElementById("content");
let img = document.querySelectorAll(".img-thumbnail");
let imgSrc; 
let index;
const getIndex = (value) =>{
    index = value;
            lightbox.style.display= null;
            imgSrc = document.getElementsByClassName("img-thumbnail")[index].src; 
            content.src = `${imgSrc}`  
        }
const closeLighbox= () =>{
    lightbox.style.display ="none";
}
btnClose.addEventListener("click", ()=>{
    closeLighbox()
});
lightbox.addEventListener("mousedown", e=>{
    if(e.target.matches("#lightbox")){
        closeLighbox()
    }
});

const nextImg = () =>{
    if (index<img.length-1) {
        index = index + 1;
    }
    else{
        index = 0;
    }
    imgSrc = document.getElementsByClassName("img-thumbnail")[index].src; 
    content.src = `${imgSrc}`  
}
const prevImg = () =>{
    if (index>0) {
        index = index - 1;
    }
    else{
        index = img.length-1;
    }
    imgSrc = document.getElementsByClassName("img-thumbnail")[index].src; 
    content.src = `${imgSrc}`  
}

let topbutton = document.getElementById("topBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

const scrollFunction=()=> {
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    topbutton.style.display = "block";
} else {
    topbutton.style.display = "none";
}
}

// When the user clicks on the button, scroll to the top of the document
const topFunction=() =>{
  document.body.scrollTop = 0; // For Safari
document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 

console.log("Working")