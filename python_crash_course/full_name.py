#!/usr/bin/env python3

first_name ="ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

full_name = "{} {}".format(first_name, last_name)
print(full_name)

print(f"\nMy full name is {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print('\nPrinted from "message" variable:')
print(message)
