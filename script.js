const form = document.getElementById("newsForm");
const input = document.getElementById("newsInput");
const error = document.getElementById("errorMsg");
const clearBtn = document.getElementById("clearBtn");

// Create live character counter
const counter = document.createElement("div");
counter.style.textAlign = "right";
counter.style.marginTop = "6px";
counter.style.fontSize = "12px";
counter.style.opacity = "0.7";
input.parentNode.insertBefore(counter, input.nextSibling);

// Update counter on typing
input.addEventListener("input", function () {
    const len = input.value.length;
    counter.textContent = `${len} / 5000 characters`;

    if (len >= 50) {
        error.textContent = "";
    }
});

// Form validation
form.addEventListener("submit", function (e) {
    if (input.value.trim().length < 50) {
        e.preventDefault();
        error.textContent = "Please enter at least 50 characters of news content.";
        error.style.color = "red";
    }
});

// Clear button
clearBtn.addEventListener("click", function () {
    input.value = "";
    error.textContent = "";
    counter.textContent = "0 / 5000 characters";
});