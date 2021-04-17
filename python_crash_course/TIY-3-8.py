#! /usr/bin/env python3

cities = ["Moscow", "Hawaii", "Anchorage", "Tonga", "Johannesburg"]

print("Cities: Original Order #1")
print(cities)

print("\nCities: Sorted using \"sorted\"")
print(sorted(cities))
print("Cities: Original Order #2")
print(cities)

print("\nCities: Sort permanently from original using \".reverse\"")
cities.reverse()
print(cities)
print("Cities: Switching back to original using \".reverse\" again")
cities.reverse()
print(cities)

print("\nCities: Sort permanently from original using \"sort\"")
cities.sort()
print(cities)
print("Cities: Switching back to original using \"sort\" again")
cities.sort(reverse=True)
print(cities)

