
let resetform = document.querySelector("#reset-password-form");
let subtn = document.querySelector("#resetsubmit");

resetform.addEventListener("submit",()=>{
    console.log("yes");
    subtn.disabled = true;
    subtn.innerText ="Sending...";
});


