// LOAD BTN

let load_btn = document.getElementById("load-btn");
let hidden_div = document.getElementById("hide-div");
let hidden_div2 = document.getElementById("hide-div2");

hidden_div.style.display = "none";
hidden_div2.style.display = "none";

load_btn.addEventListener("click", first)

function first(e){
    hidden_div.style.display = "";
    e.stopImmediatePropagation();
    this.removeEventListener("click", first);
    document.onclick = second;
}

function second(){
    hidden_div2.style.display = "";
}

// SCROLL BTN

let interval_id = 0;
let scroll_btn = document.querySelector(".scroll-btn");
let scrollPos = document.getElementsByTagName("body")[0].scrollTop;
let trendDiv = document.getElementById("trend-box").offsetTop;
// Hide scroll btn
scroll_btn.style.visibility = "hidden";

//on scroll hide/show
window.onscroll = () =>{
    if(window.pageYOffset >= 250){
        scroll_btn.style.visibility = "visible";
    }else{
        scroll_btn.style.visibility = "hidden";
    }
}

// scroll to top
function scrollToTop(){
    interval_id = setInterval(function(){
        // top of page
        if(window.pageYOffset === 0){
            clearInterval(interval_id);
        }
        window.scroll(0, window.pageYoOffset);
    }, 16.66);
}

// Call scrollToTop on click
scroll_btn.addEventListener("click", scrollToTop);
