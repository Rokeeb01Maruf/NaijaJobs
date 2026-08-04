const profile = document.querySelector(".profile")
const profiles = document.querySelector("header nav .absolute")
const overlay = document.querySelector("div.overlay")
const button = document.querySelector("div.overlay button")

if(window.innerWidth <= 780){
    overlay.style.display = "flex"
}else{
    overlay.style.display = "none"
}

button.addEventListener("click", ()=>{
    overlay.style.display = "flex"
})

profile.addEventListener("click", ()=>{
    profile.classList.toggle("active")
    profiles.classList.toggle("flex")
})
