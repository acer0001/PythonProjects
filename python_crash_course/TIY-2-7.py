#!/usr/bin/env python3

name_norm = "Forrest Gump"
name_rt = "Forrest Gump "
name_lft = " Forrest Gump"
name_both = " Forrest Gump "

print("\nRight spocing:")
print(f"Wow,{name_rt}is crazy!")
print("Remove right spocing:")
print(f"Wow,{name_rt.rstrip()}is crazy!")

print("\nLeft spocing:")
print(f"Wow,{(name_lft)}is crazy!")
print("Remove Left spocing:")
print(f"Wow,{(name_lft.lstrip())}is crazy!")

print("\nBoth spocing:")
print(f"Wow,{(name_both)}is crazy!")
print("Remove both spocing:")
print(f"Wow,{name_both.strip()}is crazy!")

print("\nShowing a TAB:")
print(f"\tWow, {name_norm} is crazy!")
