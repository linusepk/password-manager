function getPassword(id) {
    copy(accs[id].password)
}

function copy(text) {
    let temp = document.createElement("textarea");
    document.body.appendChild(temp);
    temp.value = text;
    temp.select();
    document.execCommand("copy");
    document.body.removeChild(temp);
}
