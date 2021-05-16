#! /usr/bin/env python3

usernames = []

if usernames: # If usernames has any objects at all, run the following code
    for username in usernames:
        if username == "admin":
            print(f"Hello, {username.title()}. Would you like a status report?")
        else:
            print(f"Hello, {username.title()}. Thanks you for logging in again.")
else: # If usernames has no objects, run the following code
    print("We need to find some users!")