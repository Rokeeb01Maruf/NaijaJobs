const signup = document.querySelector("#Logup")
const first = document.querySelector(".ifn")
const last = document.querySelector(".iln")
const user = document.querySelector(".iuse")
const iemail = document.querySelector(".iemail")
const ipass = document.querySelector(".ipass")
const ipassed = document.querySelector(".ipassed")
const terms = document.querySelector(".term")
signup.addEventListener("submit", (e)=>{
    if(!first.value){
        e.preventDefault()
        const error = document.querySelector(".ifirst")
        error.classList.add("display")
    }else if(!last.value){
        e.preventDefault()
        const error = document.querySelector(".ilast")
        error.classList.add("display")
    }else if(!user.value){
        e.preventDefault()
        const error = document.querySelector(".iuser")
        error.classList.add("display")
    }else if(!iemail.value.includes("@") || !iemail.value.includes(".com")){
        e.preventDefault()
        const error = document.querySelector(".ipemail")
        error.classList.add("display")
    }else if(ipass.value.length < 8){
        e.preventDefault()
        const error = document.querySelector(".ipass1")
        error.classList.add("display")
    }else if(ipass.value !== ipassed.value){
        e.preventDefault()
        const error = document.querySelector(".ipass2")
        error.classList.add("display")
    }else if(!terms.checked){
        e.preventDefault()
        const error = document.querySelector(".iread")
        error.classList.add("display")
    }
})

first.addEventListener("click", ()=>{
    const error = document.querySelector(".ifirst")
    error.classList.remove("display")
})
last.addEventListener("click", ()=>{
    const error = document.querySelector(".ilast")
    error.classList.remove("display")
})
user.addEventListener("click", ()=>{
    const error = document.querySelector(".iuser")
    error.classList.remove("display")
})
iemail.addEventListener("click", ()=>{
    const error = document.querySelector(".ipemail")
    error.classList.remove("display")
})
ipass.addEventListener("click", ()=>{
    const error = document.querySelector(".ipass1")
    error.classList.remove("display")
})
ipassed.addEventListener("click", ()=>{
    const error = document.querySelector(".ipass2")
    error.classList.remove("display")
})
terms.addEventListener("click", ()=>{
    const error = document.querySelector(".iread")
    error.classList.remove("display")
})

const eyeOn = document.querySelector(".on")
const eyeOff = document.querySelector(".off")
const eyeInput = document.querySelector(".ipass")

eyeOn.addEventListener("click", ()=>{
    eyeInput.setAttribute("type", "text")
    eyeOn.classList.add("none")
    eyeOff.classList.remove("none")
})
eyeOff.addEventListener("click", ()=>{
    eyeInput.setAttribute("type", "password")
    eyeOff.classList.add("none")
    eyeOn.classList.remove("none")
})

const see = document.querySelector(".one")
const blind = document.querySelector(".zero")
const seeInput = document.querySelector(".see-input")

see.addEventListener("click", ()=>{
    seeInput.setAttribute("type", "text")
    see.classList.add("none")
    blind.classList.remove("none")
})
blind.addEventListener("click", ()=>{
    seeInput.setAttribute("type", "password")
    see.classList.remove("none")
    blind.classList.add("none")
})