const profile = document.querySelector(".profile")
const profiles = document.querySelector("header nav .absolute")
const overlay = document.querySelector("div.overlay")
const button = document.querySelector("div.overlay button")


profile.addEventListener("click", ()=>{
    profile.classList.toggle("active")
    profiles.classList.toggle("flex")
})

console.log(window)