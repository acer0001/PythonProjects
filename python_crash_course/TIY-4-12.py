#! /usr/bin/env python3

my_foods = ["bacon", "broccoli", "pasta", "swiss cheese", "tomatoes"]
friends_foods = my_foods[:]

my_foods.append("asparagus")
friends_foods.append("oranges")

print("My recipe requires:")
for my_recipe_food in my_foods:
    print(f"-- {my_recipe_food}")

print("\nMy friend's recipe requires:")
for friend_recipe_food in friends_foods:
    print(f"-- {friend_recipe_food}")
