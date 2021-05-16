#! /usr/bin/env python3

usernames = ["admin", "bob", "joe", "sandra", "michelle"]
for username in usernames:
    if username == "admin":
        print(f"Hello, {username.title()}. Would you like a status report?")
    else:
        print(f"Hello, {username.title()}. Thanks you for logging in again.")
