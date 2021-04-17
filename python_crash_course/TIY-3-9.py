#! /usr/bin/env python3

guests = [ "Mike", "Jake", "Melinda"]

print(f"Yay! We have {len(guests)} coming for dinner!")

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

print(f"\nYay! We have {len(guests)} coming for dinner!")

print(f"\nSorry the table wasn't delivered. We can only have 2 guests... :-(")

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

print(f"\nYay! We have {len(guests)} coming for dinner!")

del guests[0]
del guests[0]


print(f"\nEveryone cancelled. I guess {len(guests)} guests are coming now...")
