const form = document.getElementById("newsForm");
const input = document.getElementById("newsInput");
const error = document.getElementById("errorMsg");
const clearBtn = document.getElementById("clearBtn");

form.addEventListener("submit", function(e){
    if(input.value.trim().length < 50){
        e.preventDefault();
        error.textContent = "Please enter at least 50 characters of news content.";
        error.style.color = "red";
    }
});

clearBtn.addEventListener("click", function(){
    input.value = "";
    error.textContent = "";
});