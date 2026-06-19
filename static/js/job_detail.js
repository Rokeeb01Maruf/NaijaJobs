const alerts = document.querySelector(".absoluted")
const buttonAuth = document.querySelector(".auth button")
const close = document.querySelector(".absoluted .alert-card section img")

buttonAuth.addEventListener("click", ()=>{
    alerts.classList.add("flex")
})

close.addEventListener("click", ()=>{
    alerts.classList.remove("flex")
})