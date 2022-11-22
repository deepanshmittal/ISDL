var logOutButton = document.getElementById("logOutButton");
if (logOutButton) {
    logOutButton.addEventListener("click", function (e) {
        window.location.href = "/logout/";
    });
}
var inventoryLocating = document.getElementById("inventoryLocating");
if (inventoryLocating) {
    inventoryLocating.addEventListener("click", function (e) {
        window.location.href = "/main-gate-inventory-manager/inventory/";
    });
}

var button2 = document.getElementById("button2");
if (button2) {
    button2.addEventListener("click", function (e) {
        window.location.href = "/main-gate-inventory-manager/exit-details/";
    });
}

var button1 = document.getElementById("button1");
if (button1) {
    button1.addEventListener("click", function (e) {
        window.location.href = "/main-gate-inventory-manager/entry-details/";
    });
}
var scrollAnimElements = document.querySelectorAll("[data-animate-on-scroll]");
var observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
        if (entry.isIntersecting || entry.intersectionRatio > 0) {
            const targetElement = entry.target;
            targetElement.classList.add("animate");
            observer.unobserve(targetElement);
        }
    }
}, {
    threshold: 0.15,
});

for (let i = 0; i < scrollAnimElements.length; i++) {
    observer.observe(scrollAnimElements[i]);
}

function getItemCode() {
    document.querySelector('#ItemCode').value = document.querySelector('input[type="radio"]:checked').value;
}

// document.getElementById("Quantity").setAttribute("max", document.getElementById("set_Quantity").value);