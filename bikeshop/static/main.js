document.addEventListener("DOMContentLoaded", ()=>{

    document.querySelector(".detail-photo-price span").addEventListener("click", ()=>{
        document.querySelector(".detail-large-img").style.display = "flex"
    })

    document.querySelector(".detail-large-img span").addEventListener("click", ()=>{
        document.querySelector(".detail-large-img").style.display = "none"
    })
    
    
    
    
    document.querySelector("#year").innerHTML = new Date().getFullYear()
})