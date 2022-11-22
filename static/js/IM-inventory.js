var itemsButton = document.getElementById("itemsButton");
if (itemsButton) {
    itemsButton.addEventListener("click", function (e) {
        window.location.href = "/inventory-manager/register-item";
    });
}

var requestPurchaseButton = document.getElementById("requestPurchaseButton");
if (requestPurchaseButton) {
    requestPurchaseButton.addEventListener("click", function (e) {
        window.location.href = "/inventory-manager/request-purchase";
    });
}

var removeInvButton = document.getElementById("removeInvButton");
if (removeInvButton) {
    removeInvButton.addEventListener("click", function (e) {
        window.location.href = "/inventory-manager/remove-inventory";
    });
}

var inventoryLocating = document.getElementById("inventoryLocating");
if (inventoryLocating) {
    inventoryLocating.addEventListener("click", function (e) {
        window.location.href = "/inventory-manager";
    });
}

var addInvButton = document.getElementById("addInvButton");
if (addInvButton) {
    addInvButton.addEventListener("click", function (e) {
        window.location.href = "/inventory-manager/add-inventory";
    });
}

var logOutButton = document.getElementById("logOutButton");
if (logOutButton) {
    logOutButton.addEventListener("click", function (e) {
        window.location.href = "/logout";
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