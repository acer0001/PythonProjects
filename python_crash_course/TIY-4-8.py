#! /usr/bin/env python3

cubes = (value**3 for value in (range(1, 11)))
for cube in cubes:
    print(f"{cube}")
