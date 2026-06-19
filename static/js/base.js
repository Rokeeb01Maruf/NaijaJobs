const profile = document.querySelector(".profile")
const profiles = document.querySelector("header nav .absolute")


profile.addEventListener("click", ()=>{
    profile.classList.toggle("active")
    profiles.classList.toggle("flex")
})