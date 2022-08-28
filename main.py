from flask import Flask, render_template, session, redirect, request
import json
import os

from pkg_resources import require
from account_manager import create_account, delete_account, get_accounts, update_account, delete_account, update_password

app = Flask(__name__)
app.secret_key = os.urandom(32)
app.session_cookie_name = "session"
app.template_folder = "website/templates"
app.static_folder = "website/static"

def check_login():
    if "logged_in" not in session or not session["logged_in"]:
        return redirect("/login")
    return True

@app.route("/login", methods=["GET", "POST"])
def login():
    status = check_login()
    if status is True:
        return redirect("/")

    if request.method == "GET":
        return render_template("login.html");


    if request.method == "POST":
        account = []
        with open("login.json", "r") as f:
            account = json.load(f)

        data = request.json
        if "username" not in data or "password" not in data:
            return {"message": "Missing argument(s)"}, 400

        if data["username"] == account["username"] and data["password"] == account["password"]:
            session["logged_in"] = True;
            return {"message": "Login successful"}, 202
        else:
            return {"message": "Invalid credentials"}, 400

@app.route("/logout")
def logout():
    session["logged_in"] = False

    return redirect("/")

@app.route("/create", methods = ["GET", "POST"])
def create():
    status = check_login()
    if status is not True:
        return status
    
    if request.method == "GET":
        return render_template("create.html")
    
    if request.method == "POST":
        data = request.json;

        if data["site"] == "" or (data["email"] == "" and data["username"] == "") != False:
            print("Invalid")
            return {}, 400

        status, password = create_account(data["site"], data["username"], data["email"])
        if status:
            return {"password": password }, 201
        else:
            return {}, 400


@app.route("/edit/<int:id>", methods = ["GET", "POST"])
def edit(id: int):
    status = check_login()
    if status is not True:
        return status

    if request.method == "GET":
        return render_template("edit.html", id=id, account=get_accounts()[id])

    if request.method == "POST":
        data = request.json
        update_account(id, {
            "site": data["site"],
            "username": data["username"],
            "email": data["email"]
        })
        return data, 200


@app.route("/search")
def search():
    status = check_login()
    if status is not True:
        return status

    site     = request.args.get("site")
    username = request.args.get("username")
    email    = request.args.get("email")
    print(site)

    accs = []
    for account in get_accounts():
        if (site == "" or site.lower() in account["site"].lower()) and (username == "" or username.lower() in account["username"].lower()) and (email == "" or email.lower() in account["email"].lower()):
            accs.append(account)

    return render_template("search.html", count=len(accs), accounts=accs)

@app.route("/delete", methods=["POST"])
def delete():
    status = check_login()
    if status is not True:
        return status

    if request.method == "POST":
        delete_account(request.json["id"])

        return {}, 200

@app.route("/update_password", methods = ["POST"])
def update_passwd():
    status = check_login()
    if status is not True:
        return status

    if request.method == "POST":
        password = update_password(request.json["id"])

        return {"password": password}, 200

@app.route("/")
def main():
    status = check_login()
    if status is not True:
        return status

    accounts = get_accounts()

    return render_template("index.html", count=len(accounts), accounts=accounts)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
