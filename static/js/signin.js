const signin = document.querySelector("#Login")
const email = document.querySelector(".inmail")
const password = document.querySelector(".inpassword")
signin.addEventListener("submit", (e)=>{
    if(!email.value){
        e.preventDefault()
        const error = document.querySelector(".pemail")
        error.classList.add("display")
    }else if(!password.value){
        e.preventDefault()
        const error = document.querySelector(".ppassword")
        error.classList.add("display")
    }
})

email.addEventListener("click", ()=>{
    const error = document.querySelector(".pemail")
        error.classList.remove("display")
})
password.addEventListener("click", ()=>{
    const error = document.querySelector(".ppassword")
        error.classList.remove("display")
})