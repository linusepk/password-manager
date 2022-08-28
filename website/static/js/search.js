function search() {
    let site = document.getElementById("site-search").value;
    let username = document.getElementById("username-search").value;
    let email = document.getElementById("email-search").value;

    location.href = "/search?site=" + site + "&username=" + username + "&email=" + email;
}

document.addEventListener("keypress", event => {
    if (event.key == "Enter") {
        event.preventDefault();
        search();
    }
});
