#! /usr/bin/env python3

# I wanted to make this interactive instead os a static variable as asked for this exercise in the book.
# I hope I get bonus credit! :-)

age = input("Enter your age to see your stage of life: ")

if int(age) < 2:
    print("You are a baby.")
elif (int(age) >= 2) and (int(age) < 4):
    print("You are an toddler.")
elif (int(age) >= 4) and (int(age) < 13):
    print("You are a kid.")
elif (int(age) >= 13) and (int(age) < 20):
    print("You are a teenager.")
elif (int(age) >= 20) and (int(age) < 65):
    print("You are an adult.")
else:
    print("You are a senior citizen.")