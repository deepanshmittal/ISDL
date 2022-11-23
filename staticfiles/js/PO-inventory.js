var logOutButton = document.getElementById("logOutButton");
if (logOutButton) {
    logOutButton.addEventListener("click", function (e) {
        window.location.href = "/logout";
    });
}

var button3 = document.getElementById("button3");
if (button3) {
    button3.addEventListener("click", function (e) {
        window.location.href = "/purchase-officer/request-history/";
    });
}
var invertory_location = document.getElementById("invertory-location");
if (invertory_location) {
    invertory_location.addEventListener("click", function (e) {
        window.location.href = "/purchase-officer/inventory/";
    });
}
var button1 = document.getElementById("button1");
if (button1) {
    button1.addEventListener("click", function (e) {
        window.location.href = "/purchase-officer/pending-request/";
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