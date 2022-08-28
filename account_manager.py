import json
import string
import random

with open("accounts.json", "r") as f:
    accounts = json.load(f)

def gen_password():
    available = string.ascii_letters + string.digits
    password = ""
    for i in range(32):
        password += available[random.randrange(0, len(available))]
    
    return password

def create_account(site: str, username: str, email: str):
    account = {
        "site": site,
        "username": username,
        "email": email,
        "password": gen_password()
    }

    if account_exists(account):
        return (False, None)

    accounts.append(account)

    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4)

    return (True, account["password"])

def account_exists(account):
    for acc in accounts:
        if acc["username"] == account["username"] and acc["email"] == account["email"] and acc["site"] == account["site"]:
            return True
        else:
            return False

def get_accounts():
    return accounts

def update_account(id, account):
    accounts[id]["site"] = account["site"]
    accounts[id]["username"] = account["username"]
    accounts[id]["email"] = account["email"]

    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4)

def delete_account(id):
    accounts.pop(id)

    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4)

def update_password(id):
    accounts[id]["password"] = gen_password()

    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4)

    return accounts[id]["password"]
