var logOutButton = document.getElementById("logOutButton");
if (logOutButton) {
    logOutButton.addEventListener("click", function (e) {
        window.location.href = "/logout/";
    });
}

var button3 = document.getElementById("button3");
if (button3) {
    button3.addEventListener("click", function (e) {
        window.location.href = "/purchase-officer/request-history/";
    });
}

var button1 = document.getElementById("button1");
if (button1) {
    button1.addEventListener("click", function (e) {
        window.location.href = "./";
    });
}

var inventoryLocating = document.getElementById("inventoryLocating");
if (inventoryLocating) {
    inventoryLocating.addEventListener("click", function (e) {
        window.location.href = "/purchase-officer/inventory/";
    });
}

var deleteButtonContainer = document.getElementById("deleteButtonContainer");
if (deleteButtonContainer) {
    deleteButtonContainer.addEventListener("click", function () {
        //TODO: Clear the selection or reload
    });
}

var deleteButton = document.getElementById("deleteButton");
if (deleteButton) {
    deleteButton.addEventListener("click", function () {
        //TODO: Clear the selection or reload
    });
}
var scrollAnimElements = document.querySelectorAll("[data-animate-on-scroll]");
var observer = new IntersectionObserver(
    (entries) => {
        for (const entry of entries) {
            if (entry.isIntersecting || entry.intersectionRatio > 0) {
                const targetElement = entry.target;
                targetElement.classList.add("animate");
                observer.unobserve(targetElement);
            }
        }
    },
    {
        threshold: 0.15,
    }
);

for (let i = 0; i < scrollAnimElements.length; i++) {
    observer.observe(scrollAnimElements[i]);
}


function ClearRadio(RadioName) {
    var ele = document.getElementsByName(RadioName);
    for (var i = 0; i < ele.length; i++)
        ele[i].checked = false;
}

function getRegNo() {
    document.querySelector('#RegNo').value = document.querySelector('input[type="radio"]:checked').value;
}