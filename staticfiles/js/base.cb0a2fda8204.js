const profile = document.querySelector(".profile")
const profiles = document.querySelector("header nav .absolute")
const overlay = document.querySelector("div.overlay")
const button = document.querySelector("div.overlay button")

function makeResponsive(){
    const width = window.innerWidth

    if (width < 768){
        overlay.style.display = "flex"
    }else{
        overlay.style.display = "none"
    }
}

button.addEventListener("click", ()=>{
    overlay.setAttribute("style", "display: flex;")
})

window.addEventListener("resize", makeResponsive)
makeResponsive()


profile.addEventListener("click", ()=>{
    profile.classList.toggle("active")
    profiles.classList.toggle("flex")
})
