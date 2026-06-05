const buttons = document.querySelectorAll(".category button")
const profile = document.querySelector(".profile")

for (let i=0; i<buttons.length; i++){
    buttons[i].addEventListener("click", ()=>{
        buttons.forEach((e)=>{
            e.classList.remove("selected")
        })
        buttons[i].classList.add("selected")
    })
}

profile.addEventListener("click", ()=>{
    profile.classList.toggle("active")
})