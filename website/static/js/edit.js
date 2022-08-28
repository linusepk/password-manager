function edit(id, update_passwd = false) {
    let site     = document.getElementById("site").value;
    let username = document.getElementById("username").value;
    let email    = document.getElementById("email").value;

    data = {
        "site": site,
        "username": username,
        "email": email,
    }

    fetch("/edit/" + id, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (response.ok && !update_passwd) {
            location.href = "/";
        }
        
        return response.ok;
    });
}

function updatePassword(id) {
    edit(id, true);

    fetch("/update_password", {
        method: "POST",
        body: JSON.stringify({"id": id}),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (response.ok) {
            console.log(response.json().then(data => {
                copy(data.password);
                // console.log(data.password);
            }).then(() => location.href = "/"));
        }
    });
}

function del(id) {
    fetch("/delete", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({"id": id})
    })
    .then(response => {
        if (response.ok) {
            location.href = "/";
        }

        console.log(response);
    });
}

document.addEventListener("keydown", event => {
    if (event.key == "Enter") {
        event.preventDefault();
        edit(_id);
    }
});
