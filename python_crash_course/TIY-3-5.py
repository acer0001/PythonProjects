#! /usr/bin/env python3

guests = [ "Mike", "Jake", "Melinda"]

print(f"\n{guests[2].title()}, sorry to hear you cannot come...")
del guests[2]

guests.append("Maria")

print(f"\n{guests[0].title()}, thanks for your RSVP for dinner!")
print(f"\n{guests[1].title()}, thanks for your RSVP for dinner!")
print(f"\n{guests[2].title()}, thanks for your RSVP for dinner!")