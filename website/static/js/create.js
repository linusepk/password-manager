function create() {
    let site = document.getElementById("site").value;
    let username = document.getElementById("username").value;
    let email = document.getElementById("email").value;
    data = {
        "site": site,
        "email": email,
        "username": username
    };

    fetch("/create", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (response.status == 400) {
            location.href = "/create";
        } else {
            response.json().then(data => {
                copy(data.password);
            }).then(() => location.href = "/");
        }
    });
}

document.addEventListener("keypress", event => {
    if (event.key == "Enter") {
        event.preventDefault();
        create();
    }
});
