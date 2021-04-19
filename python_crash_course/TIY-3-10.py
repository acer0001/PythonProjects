#! /usr/bin/env python3

cameras = ["canon", "minolta", "bronica", "pentax", "nikon", "yashica"]

print("This is an example of a accessing elements in a list [3].")
print(f"My favorite camera: {cameras[3].title()}")

print("\nThis is an example of last item in a list.")
print(f"One of the cameras I don't own is: {cameras[-1].title()}")

print("\nThis is an example of replacing an item in a list.")
cameras[4] = "rolliflex"
print(f"I sold a camera and bought a {cameras[4].title()}.")

print("\nThis is an example of appending an item to the end of a list.")
cameras.append("hasselblad")
print(cameras)
print(f"I don't ever think I'll own a {cameras[-1].title()}.")

print("\nThis is an example of inserting an item to a list [2].")
cameras.insert(2, "mamiya")
print(cameras)
print(f"The {cameras[2].title()} is also a medium format camera.")

print("\nThis is an example of permanently deleting an item to a list [3].")
del cameras[3]
print(cameras)
print(f"I sold a camera, but didn't buy one.")

print("\nThis is an example of removing an item to a list [2] and assigning to a variable.")
removed_camera = cameras.pop(2)
print(cameras)
print(f"I sold my {removed_camera.title()} yesterday.")

print("\nThis is an example of removing an item to a list [2] by string instead of position.")
cameras.remove("rolliflex")
print(cameras)
print("I removed the only TLR I know about.")

print("\nThis is an example of removing a string to a variable, removing it and working with it after removal.")
sold_camera = "yashica"
cameras.remove(sold_camera)
print(cameras)
print(f"I sold my {sold_camera.title()} for a boatload of money!")

print("\nThis is an example of temporarily sorting items in a list (sorted).")
cameras_sorted = sorted(cameras)
print(f"These are temporarily alphabetically sorted cameras: \n{cameras_sorted}")
print(f"These are the original sorted cameras: \n{cameras}")

print("\nThis is an example of permanently sorting items in a list (sort).")
cameras.sort()
print(f"These are permanently alphabetically sorted cameras: \n{cameras}")

print("\nThis is an example of permanently reverse sorting items in a list (sort).")
cameras.sort(reverse = True)
print(f"These are permanently alphabetically reverse sorted cameras: \n{cameras}")

print("\nThis is an example of counting items in a list (len).")
print(cameras)
print(f"I have {len(cameras)} cameras in my inventory.")
