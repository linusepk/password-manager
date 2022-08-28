function login() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    data = {
        "username": username,
        "password": password
    };

    fetch("/login", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(() => location.href = "/");
}

document.addEventListener("keypress", event => {
    if (event.key == "Enter") {
        event.preventDefault();
        login();
    }
});
