#! /usr/bin/env python3

bike = 'cannondale'
print("Is the bike brand a Giant? I predict False.")
print(bike == 'giant')

print("\nIs the bike brand a cannondale? I predict True.")
print(bike == 'cannondale')

bike = 'Cannondale'
print("\nIs the bike brand a Canondale? I predict True")
print(bike.lower() == 'cannondale')

bike = 'Specialized'
print("\nIs the bike a Specialized? I predict False.")
print(bike.lower() == 'specialized')

number = 25
print("\nIs 22 equal to 25? I predict False.")
print(number == 22)

print("\nIs 22 not equal to 25? I predict True.")
print(number != 22)

print("\nIs 22 greater than 25? I predict False.")
print(22 > number)

print("\nIs 22 less than 25? I predict True.")
print(number > 22)

print("\nIs 22 less than or equal to 25? I predict True.")
print(22 <= number)

print("\nIs 22 greater than or equal to 25? I predict False.")
print(number <= 22)

print("\nIs 18 or 22 greater than 25? I predict False.")
print((number < 18) or (number < 22))

print("\nIs 18 or 22 less than 25? I predict True.")
print((number > 18) or (number > 22))

print("\nIs 18 or 28 greater than 25? I predict True.")
print((number > 18) or (number > 28))

print("\nIs 18 or 28 less than 25? I predict True.")
print((number < 18) or (number < 28))

print("\nIs 22 and 28 less than 25? I predict False.")
print((number < 22) and (number < 28))

print("\nIs 18 and 28 more than 25? I predict False.")
print((number > 18) and (number > 28))

foods = ["pizza", "cookies", "burgers", "donuts"]
print(f"\nMy food list: {foods}")
print('\nIs" "donuts" in the list?')
print('donuts' in foods)

print('\nIs "meatloaf" in the list?')
print('meatloaf' in foods)

bitter_food = 'brussell sprouts'
print('\nIs "brussel sprouts" on the Chef\'s list?')
if bitter_food in foods:
    print(f'Hey Chef... if so, yes! {bitter_food} for me!')
else:
    print(f'Hey Chef... If not, no {bitter_food} for me!')



