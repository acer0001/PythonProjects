#! /usr/bin/env python3

# I wanted to make this interactive instead os a static variable as asked for this exercise in the book.
# I hope I get bonus credit! :-)

fave_fruits = ["banana", "orange", "kiwi", "pineapple"]

guessed_fruit = input("Guess my favorite fruits: ")

if guessed_fruit in fave_fruits:
    print("Yes, that is one of my favorites!")
if guessed_fruit not in fave_fruits:
    print("Nope, that fruit is yucky.")
