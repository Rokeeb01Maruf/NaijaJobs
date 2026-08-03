const jobcards = document.querySelectorAll("div.job-cards")
const hidden = document.querySelector("form button.job-cards input[type='hidden']")

jobcards.forEach((jobcard)=>{
    jobcard.addEventListener("click", ()=>{
        jobcard.classList.toggle("select")
    })
})