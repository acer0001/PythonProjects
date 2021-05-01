#! /usr/bin/env python3

times_three_multiples = (number*3 for number in (range(1, 31)))
for times_three_multiple in times_three_multiples:
    print(f"{times_three_multiple}")
