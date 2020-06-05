function foo(imgs) {
    var mainImage = document.getElementById("main-image");
    mainImage.src = imgs.src;
    mainImage.parentElement.style.display = "block";
}