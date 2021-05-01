#! /usr/bin/env python3

my_pizzas = ["supreme", "meat lovers", "veggie lovers", "plain cheese"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("cowboy")
print("Adding cowboy to my_pizzas...")
print(my_pizzas)

friend_pizzas.append("spicy")
print("\nAdding spicy to friend_pizzas...")
print(friend_pizzas)

print(f"\nMy favorite pizzas are:")
for my_pizza in my_pizzas:
    print(f"{my_pizza.title()}")

print(f"\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(f"{friend_pizza.title()}")
