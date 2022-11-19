var logOutButton = document.getElementById("logOutButton");
if (logOutButton) {
    logOutButton.addEventListener("click", function (e) {
        window.location.href = "./Home.html";
    });
}

var itemsButton = document.getElementById("itemsButton");
if (itemsButton) {
    itemsButton.addEventListener("click", function (e) {
        window.location.href = "./AddNewItem.html";
    });
}

var addInvButton = document.getElementById("addInvButton");
if (addInvButton) {
    addInvButton.addEventListener("click", function (e) {
        window.location.href = "./AddInv.html";
    });
}

var requestPurchaseButton = document.getElementById("requestPurchaseButton");
if (requestPurchaseButton) {
    requestPurchaseButton.addEventListener("click", function (e) {
        window.location.href = "./RquestPurchase.html";
    });
}

var removeInvButton = document.getElementById("removeInvButton");
if (removeInvButton) {
    removeInvButton.addEventListener("click", function (e) {
        window.location.href = "./RemoveInv.html";
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