#! /usr/bin/env python3

guests = [ "Mike", "Jake", "Melinda"]

print(f"\n{guests[2].title()}, sorry to hear you cannot come...")
del guests[2]

guests.append("Maria")

print(f"\n{guests[0].title()}, thanks for your RSVP for dinner!")
print(f"\n{guests[1].title()}, thanks for your RSVP for dinner!")
print(f"\n{guests[2].title()}, thanks for your RSVP for dinner!")

print("\nGuess what? We found a bigger table. Inviting more guests!")

guests.insert(0, "Bubba")
guests.insert(3, "Jodi")
guests.insert(5, "Ralph")

print(f"\n{guests[0].title()}, thanks for your RSVP for dinner!")
print(f"\n{guests[3].title()}, thanks for your RSVP for dinner!")
print(f"\n{guests[5].title()}, thanks for your RSVP for dinner!")

print("\nSorry the table wasn't delivered. We can only have two guests... :-(")

guests_last = guests.pop()
print(f"\nMaybe next time {guests_last.title()}...")
guests_last = guests.pop()
print(f"\nMaybe next time {guests_last.title()}...")
guests_last = guests.pop()
print(f"\nMaybe next time {guests_last.title()}...")
guests_last = guests.pop()
print(f"\nMaybe next time {guests_last.title()}...")

print(f"\n{guests[0].title()}, you are still invited to dinner!")
print(f"\n{guests[1].title()}, you are still invited to dinner!")

del guests[0]
del guests[0]

print(f"\nI guess {len(guests)} guests are coming now...")
