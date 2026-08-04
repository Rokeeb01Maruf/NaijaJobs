const profile = document.querySelector(".profile")
const profiles = document.querySelector("header nav .absolute")
const overlay = document.querySelector("div.overlay")
const button = document.querySelector("div.overlay button")

window.addEventListener("load", ()=>{
    if(window.innerWidth <= 780){
        overlay.style.display = "flex"
    }else{
        overlay.style.display = "none"
    }
})

profile.addEventListener("click", ()=>{
    profile.classList.toggle("active")
    profiles.classList.toggle("flex")
})
