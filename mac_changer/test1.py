#! //usr/bin/env python3

import random

def gen_rand_digit():
    hex_list = ["0", "1", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    rand_digit = random.choice(hex_list)
    return rand_digit

digits = []
for d in range(0, 12):
    digits = gen_rand_digit()
    print(digits)

# print(':'.join(digits))