const container = document.querySelector(".container")
const create = document.querySelector(".head button")
const overlay = document.querySelector(".overlay")
const overlayForm = document.querySelector(".overlay form")
const x = document.querySelector(".overlay form header img")
const closing = document.querySelector(".overlay form footer button:first-child")
const forming = document.querySelector(".overlay form")

create.addEventListener("click", ()=>{
    overlay.classList.add("flex")
})

closing.addEventListener("click", ()=>{
    overlay.classList.remove("flex")
})

x.addEventListener("click", ()=>{
    overlay.classList.remove("flex")
})

forming.addEventListener("submit", (e)=>{
    const data = new FormData(e.target)
    const title = data.get("title")
    const jobType = data.get("job_type")
    const salaryMin = data.get("min_salary")
    const salaryMax = data.get("max_salary")
    const description = data.get("description")
    const category = data.get("category")
    const dateClosing = data.get("date_closing")
    function defineError(a){
        const error = document.createElement("p")
        error.textContent = a
        error.className = "error"
        container.insertBefore(error, overlay)
    }
    if(!title){
        e.preventDefault()
        clearTimeout(setTimeout(()=>defineError("Please input the job title"), 1000))
    }
})

