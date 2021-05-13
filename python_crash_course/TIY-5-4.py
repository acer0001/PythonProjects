#! /usr/bin/env python3

# I wanted to make this interactive instead os a static variable as asked for this exercise in the book.
# I hope I get bonus credit! :-)

alien_color = input("Guess an alien color: ")

if alien_color == "red":
    print("You guessed right - RED. You get 5 points!")
else:
    print("You guessed a color other than RED. You get 10 points.")
