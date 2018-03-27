// LOAD BTN 

let load_btn = document.getElementById("load-btn");
let hidden_div = document.getElementById("hide-div");
let hidden_div2 = document.getElementById("hide-div2");

hidden_div.style.display = "none";
hidden_div2.style.display = "none";

load_btn.addEventListener("click", first)

// 1rst load click
function first(e){
    hidden_div.style.display = "";
    e.stopImmediatePropagation();
    this.removeEventListener("click", first);
    document.onclick = second;
}

// 2nd load click
function second(){
    hidden_div2.style.display = "";
}
