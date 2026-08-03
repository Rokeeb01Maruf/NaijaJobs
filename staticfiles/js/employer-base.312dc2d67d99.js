const links = document.querySelectorAll(".bg")
const url = window.location.pathname.split("/")[2]

links.forEach((e, index)=>{
    const text = e.innerText.toLowerCase()
    if(text === url.toLowerCase()){
        for (let i = 0; i < url.length; i++){
            if(links[i]){
                links[i].classList.remove("bg-op")
            }
        }
        links[index].classList.add("bg-op")
    }
})

const openBtn = document.querySelector(".pro .btn")
const insertProfile = document.querySelector(".profile-fill")
const close = document.querySelectorAll(".close")

if(openBtn){
    openBtn.addEventListener("click", ()=>{
        insertProfile.classList.add("flex")
    })
}

close.forEach((e)=>{
    e.onclick=()=>{
        insertProfile.classList.remove("flex")
    }
})

const form = document.querySelector(".profile-fill form")

if(form){
    form.addEventListener("submit", (e)=>{
        const name = form.querySelector("#name")
        const industry = form.querySelector("#industry")
        const location = form.querySelector("#location")
        const website = form.querySelector("#website")
        const aboutUs = form.querySelector("#about-us")
        const email = form.querySelector("#email")
        const phone = form.querySelector("#phone")
        const linkedin = form.querySelector("#Linkedin")
        const office = form.querySelector("#office")
    
        const data = [name, industry, location, website, aboutUs, email, phone, linkedin, office]
    
        for(let i = 0; i < data.length; i++){
            data[i].addEventListener("click", ()=>{
                data[i].classList.remove("error")
            })
            if( !data[i].value){
                e.preventDefault()
                data[i].classList.add("error")
                return
            }else if(i == 3 && !data[i].value.includes("https://www.")){
                e.preventDefault()
                data[i].classList.add("error")
                return
            }else if(i == 5){
                if(!data[i].value.includes("@") || !data[i].value.includes(".com")){
                    e.preventDefault()
                    data[i].classList.add("error")
                    return
                }
            }else if(i == 6 && !data[i].value.startsWith("0")){
                e.preventDefault()
                data[i].classList.add("error")
                return
            }else if(i == 7 && !data[i].value.includes("https://")){
                e.preventDefault()
                data[i].classList.add("error")
                return
            }
        }
    })
}
