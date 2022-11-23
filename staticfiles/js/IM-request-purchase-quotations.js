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
    observer.observe(scroll9AnimElements[i]);
}
// var x= document.getElementById("proceed-button");
// x.addEventListener("mouseover", myfunc);

// if (document.getElementById("amount1")>)
// function myfunc() {
//     var amnt = document.getElementById("amount1");
//     // if(document.getElementById("amount1") >= 25000) {
//     if (amnt >= 25000) {
//         // if(>= 25000) {
//         document.getElementById("amount2").required = true;
//         // change('amount2', 'required');
//     } else {
//         document.getElementById("amount2").required = false;
//     }
//
// }