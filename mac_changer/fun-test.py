#! //usr/bin/env python3

first_number = input("What is your first number? ")
second_number = input("What is your second number? ")
operand = input("What do you want to do? [+,-,/,*] ")

if operand == '+':
    print("Your answer is: ", int(first_number) + int(second_number))
elif operand == '-':
    print("Your answer is: ", int(first_number) - int(second_number))
elif operand == '*':
    print("Your answer is: ", int(first_number) * int(second_number))
else:
    print("Your answer is: ", int(first_number) / int(second_number))
