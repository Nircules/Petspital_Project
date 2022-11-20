// This function will resize the nav bar element and font.
function myFunction() {
    const navbar = document.getElementById("trapezoid");
    const navbar_links = document.getElementById("linksUL");
    const content = document.getElementById("primary_content")
    const width = window.innerWidth;
    const screen_width = window.screen.width;
    if (width <= 550) {
        navbar.style.borderBottomWidth = "390px";
        navbar_links.style.fontSize = "10px";
    } else if (width <= 626) {
        navbar.style.borderBottomWidth = "390px";
        content.style.marginTop = "320px";
        navbar_links.style.fontSize = "14px";
    } else if (width <= 0.48 * screen_width) {
        navbar.style.borderBottomWidth = "310px";
        content.style.marginTop = "240px";
        navbar_links.style.fontSize = "16px";
    } else if (width <= 0.84 * screen_width) {
        navbar.style.borderBottomWidth = "230px";
        content.style.marginTop = "160px";
        navbar_links.style.fontSize = "16px";
    } else {
        navbar.style.borderBottomWidth = "150px";
        content.style.marginTop = "80px";
        navbar_links.style.fontSize = "16px";
    }
}

function windowW() {
    window.alert(window.innerWidth)
}

// errorslist = document.getElementsByClassName("errorlist")
// new_td = document.createElement("td")
// new_td.appendChild(errorslist)