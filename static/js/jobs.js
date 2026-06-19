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
    const error = document.querySelector(".container .error")
    // e.preventDefault()
    console.log(data, title, jobType, salaryMax, salaryMin, description, category, dateClosing)
    function defineError(a){
        error.textContent = a
        error.classList.add("show")
        setTimeout(()=> error.classList.remove("show"), 1000)
    }
    container.insertBefore(error, overlay)
    if(!title){
        e.preventDefault()
        defineError("Please input the job title")
        return
    }else if(!jobType){
        e.preventDefault()
        defineError("Please input the job type")
        return
    }else if(!salaryMin){
        e.preventDefault()
        defineError("Please input the Salary(min)")
        return
    }else if(!salaryMax){
        e.preventDefault()
        defineError("Please input the Salary(max)")
        return
    }else if(salaryMax < salaryMin){
        e.preventDefault()
        defineError("Salary(max) cannot be less that Salary(Min)")
        return
    }else if(!description){
        e.preventDefault()
        defineError("Please input the job description")
        return
    }else if(!category){
        e.preventDefault()
        defineError("Please input the job category")
        return
    }else if(!dateClosing){
        e.preventDefault()
        defineError("Please input the Application deadline")
        return
    }
})

