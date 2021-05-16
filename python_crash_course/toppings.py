#! /usr/bin/env python3

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry. All out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}...")

print("\nFinished making your pizza!")

print("<<NEW SECTION>>")
print()

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"\nAdding {requested_topping}.")
    print("Finished making your pizza!")
else:
    print("Are you sure you want just crust and sauce?")

print("<<NEW SECTION>>")
print()

available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("Finished making your pizza!")

