let loginBTN = document.getElementById("loginBTN");
let username = document.getElementById("username");
let password = document.getElementById("password");

function LoginClick() {
    redBorder();
}

function redBorder() {
    username.style.borderColor = "#eb3f48";
    password.style.borderColor = "#eb3f48";

    setTimeout(() => {
        username.style.borderColor = "#bcb2e9";
        password.style.borderColor = "#bcb2e9";;
    }, 2000);
}

function login(user, password) {
    window.location.href = "C:/bPanel/panel/panel/index.html";
}

function checkFileExist(urlToFile) {
    var xhr = new XMLHttpRequest();
    xhr.open('HEAD', urlToFile, false);
    try {
        xhr.send();
        return true;
    } catch (err) {
        return false;
    }
}