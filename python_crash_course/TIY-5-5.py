#! /usr/bin/env python3

# I wanted to make this interactive instead os a static variable as asked for this exercise in the book.
# I hope I get bonus credit! :-)

guessed_color = input("Guess an alien color: ")

if guessed_color == "green":
    print("You guessed green. You get 5 points!")
elif guessed_color == "yellow":
    print("You guessed yellow. You get 10 points")
elif guessed_color == "red":
    print("You guessed red. You get 15 points!")
else:
    print("Aliens come in only green, yellow or red...")
